from flask import Flask,render_template,url_for,redirect
from ecommerce import app
from ecommerce.forms import LoginForm,RegistrationForm
from ecommerce.models import User


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        return redirect('home')
    return render_template('register.html',form=form)

@app.route("/Login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)