from market import app, db
from market.models import Item, User
from flask import render_template, redirect, url_for, flash
from market.forms import RegisterForm
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("home_page"))
    
    form = RegisterForm()
    
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email_address=form.email_address.data).first()
        if existing_user:
            flash('This email already exists. Please try logging in', 'danger')
            return redirect(url_for('register_page'))
        
       
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=generate_password_hash(form.password.data)  
        )
        db.session.add(user_to_create)
        db.session.commit()

       
        # login_user(user_to_create)ss
        flash('Account created successfully! You are now logged in.', 'success')

        return redirect(url_for('market_page'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            print(f'there was  a error message  with creating  a user:{err_msg}')
    
    return render_template("register.html", form=form)
