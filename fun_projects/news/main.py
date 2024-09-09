from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os
from supabase import create_client, Client
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()  

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("SUPABASE_URL and SUPABASE_KEY must be set in the .env file.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
app.secret_key = os.getenv('123', 'your_default_secret_key')

@app.route("/")
def home():
    return "Hello, World!"


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        hashed_password = generate_password_hash(password, method="sha256")

        data = supabase.table("User").insert({"username": username, "email": email, "password": hashed_password}).execute()
        

        if not data:
            return redirect(url_for("login"))

    return render_template("register.html"),


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form["password"]
        email = request.form["email"]

        response = supabase.table("User").select("*").eq("email", email).execute()
        users = response.data

        if not users:
            return "No user found with that email.", 400

        user = users[0]

        if check_password_hash(user["password"], password):
            session["user_id"] = user["user_id"]
            session["username"] = user["username"]
            return redirect(url_for("profile"))

        return "Invalid credentials.", 400
    return render_template('login.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    
    # Fetch user data
    response = supabase.table('User').select('*').eq('user_id', user_id).single().execute()
    user = response.data
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        # Update user in Supabase
        update_response = supabase.table('User').update({
            'username': username,
            'email': email
        }).eq('user_id', user_id).execute()
        
        if update_response.error:
            return f"Error: {update_response.error.message}", 400
        return redirect(url_for('profile'))
    
    return render_template('profile.html', user=user)


@app.route('/recommend_news', methods=['GET', 'POST'])
def recommend_news():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    
    news = recommend_titles(user_id)
    
    return render_template('recommend_news.html', news=news)
    




@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))



def fetch_random_news():
   
    response = requests.get('https://riad-news-api.vercel.app/api/news')
    
    if response.status_code == 200:
    
        data = response.json()
    else:
        print(f"Error: {response.status_code}") 
    
    
    titles = [ item['title'] for item in data['data']]
    
    return titles

@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method == 'POST':
        selected_news = request.form.getlist('selected_news')

      
        user_id = session.get('user_id')
        
        if not user_id:
            return redirect(url_for('login'))

        for title in selected_news:
            response = supabase.table("User_Interactions").select("*").eq("user_id", user_id).eq("news_title", title).execute()
            interaction = response.data

            if interaction:
           
                interaction_count = interaction[0]['interaction_count'] + 1
                supabase.table('User_Interactions').update({
                    'interaction_count': interaction_count,
                    'last_interaction': 'now()'  
                }).eq('user_id', user_id).eq('news_title', title).execute()
            else:
              
                supabase.table('User_Interactions').insert({
                    'user_id': user_id,
                    'news_title': title,
                    'interaction_count': 1,
                    'last_interaction': 'now()'
                }).execute()

        return redirect(url_for('profile'))
    



  
    news_titles = fetch_random_news()
    return render_template('news.html', news_titles=news_titles)


def recommend_titles(user_id):
    
    response = supabase.table("User_Interactions").select("news_title").eq("user_id", user_id).execute()
    user_titles = [item['news_title'] for item in response.data]
    
    if not user_titles:
        return []

    
    all_titles = fetch_random_news()  
    
   
    combined_titles = user_titles + all_titles
    
    # TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(combined_titles)
    
    #  cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[:len(user_titles)], tfidf_matrix[len(user_titles):])
    
    
    avg_sim = cosine_sim.mean(axis=0)
    recommended_indices = np.argsort(avg_sim)[::-1][:4] #  top 4
    
    recommended_titles = [all_titles[i] for i in recommended_indices]
    
    return recommended_titles




if __name__ == "__main__":
    app.run(debug=True)
