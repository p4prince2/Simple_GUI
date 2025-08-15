from flask import Flask, render_template, request
from werkzeug.utils import redirect
from db import Database
import api

app=Flask(__name__)

dbo=Database()

@app.route('/')
def index():
    return  render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get("user_name")
    email=request.form.get("user_email")
    password= request.form.get("user_password")
    response=dbo.insert(name,email, password)
    if response :
        return render_template('login.html' , messages="Registration Successful. Kindly login to proced")
    else:
        return render_template('register.html',messages='Email already exists')


@app.route('/perform_login',methods=['post'])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response=dbo.search(email, password)
    if response:
        return redirect('/profile')
    else:
        return render_template('login.html' ,messages="incorrect email/   password")


@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return  render_template('ner.html')

@app.route('/Sentiment_Analysis')
def Sentiment_Analysis():
    return  render_template('Sentiment_Analysis.html')

@app.route('/Code_Generation')
def Code_Generation():
    return  render_template('Code_Generation.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner_route():
    text = request.form.get('ner_text')
    target = request.form.get('target_text')
    response = api.ner(text, target)
    return response

@app.route('/perform_Sentiment_Analysis',methods=['post'])
def perform_sentiment_analysis_route():
    text = request.form.get('Sentiment_Analysis_text')
    response = api.Sentiment_Analysis(text)
    return response

@app.route('/perform_Code_Generation',methods=['post'])
def perform_code_generation_route():
    text = request.form.get('Code_Generation_text')
    response = api.Code_Generation(text)
    return response


app.run(debug=True)