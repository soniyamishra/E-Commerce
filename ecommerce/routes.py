from flask import Flask,render_template,url_for,redirect
from ecommerce import app
from ecommerce.forms import LoginForm,RegistrationForm
from ecommerce.models import User


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/product")
def product():
    return render_template('product.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/view_products")
def view_products():
    return render_template('view_all_products.html')

@app.route("/add_products")
def add_products():
    return render_template('add_product.html')

@app.route("/add_category")
def add_category():
    return render_template('admin_category.html')

@app.route("/view_message")
def view_message():
    return render_template('view_message.html')

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

