import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- Find PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            webs = webs_text.get()
            if webs in data:
                email = data[webs]["email"]
                password = data[webs]["password"]
                messagebox.showinfo(title= "Found", message= f"Your Email is {email} and password {password}")
            else:
                messagebox.showerror(title= "Error", message= "No Website was found")
    except FileNotFoundError:
        messagebox.showerror(title= "Error", message= "No Website was found")
        

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    
    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)   
    temp = "".join(password)
    pass_text.insert(0,temp)
    pyperclip.copy(temp)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = webs_text.get()
    email = username_text.get()
    password = pass_text.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file, indent= 4)
        else:        
            with open("data.json", "w") as data_file:
                json.dump(data,data_file, indent= 4)
            webs_text.delete(0, "end")
            pass_text.delete(0, "end")
                
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

#Labels
webs_label = tk.Label(text= "Website:")
username_label = tk.Label(text= "Email/Username:")
pass_label = tk.Label(text= "Password:")
#Image
img = tk.PhotoImage(file= "logo.png")

canvas = tk.Canvas(height= 200, width= 200,highlightthickness= 0)
canvas.create_image(100,100,image= img )
#Buttons
generat_but = tk.Button(text= "Generate Password",width= 15,command= generate_password)
add_but = tk.Button(text= "Add", width= 30, command= save)
search_button = tk.Button(text="Search",width= 15, command= find_password)
#Entries
webs_text = tk.Entry(width= 35)
username_text = tk.Entry(width= 35)
pass_text = tk.Entry(width= 16)

canvas.grid(column= 1,row= 0)

webs_label.grid(row= 1) 
username_label.grid(row= 2) 
pass_label.grid(row= 3)  

webs_text.grid(column= 1,row= 1,columnspan= 1)
username_text.grid(column= 1,row= 2,columnspan= 2)
pass_text.grid(column= 1,row= 3)

generat_but.grid(column= 2,row= 3)
add_but.grid(column= 1,row= 4,columnspan= 2)
search_button.grid(column= 2,row= 1,columnspan= 1)












window.mainloop()