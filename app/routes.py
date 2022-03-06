
from crypt import methods
from app import app
from flask import render_template
from app import forms
from app.forms import LoginForm, RegistrationForm


@app.route('/')
@app.route('/index')
def index():

    return render_template ('index.html',title = 'home')

@app.route('/login', methods = ['GET', 'POST'])    
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods = ['GET', 'POST'])    
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)    
