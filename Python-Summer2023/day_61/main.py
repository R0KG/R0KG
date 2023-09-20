from flask import Flask,request,render_template
import requests
from wtforms import Form, StringField, EmailField, TextAreaField, validators,PasswordField,SubmitField
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5


class ContactForm(FlaskForm):
    email = EmailField("Email", validators=[validators.Length(min=6),validators.Email()])
    password = PasswordField("Password", validators= [validators.Length(min=6)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.config['SECRET_KEY'] ="123"
csrf = CSRFProtect(app)
Bootstrap5(app)


@app.route("/login", methods=["GET","POST"])
def login():
    form = ContactForm( )
    if form.validate_on_submit():
        print(form.email.data)
        return render_template("index.html",form=form)
    return render_template("denied.html")




@app.route("/")
def home():
    return render_template("start.html")
    








if __name__ == "__main__":
    app.run(debug=True)