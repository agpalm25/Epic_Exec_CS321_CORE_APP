from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from .models import Admin
from website import db

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
                        
        existing_admin = Admin.query.filter_by(email=email).first()
        if existing_admin:
            return redirect(url_for('auth.signin'))
            
        admin = Admin(email=email)
        admin.set_password(password)
        
        db.session.add(admin)
        db.session.commit()
        return redirect(url_for('auth.signin'))
       
    return render_template("signup.html")


@auth_blueprint.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(email=email).first()
        if admin and admin.check_password(password):
            login_user(admin)
            return redirect(url_for('main.admin_home'))
    
    return render_template("signin.html")

@auth_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('auth.signin'))

@auth_blueprint.route("/forgot-password")
def forgot_password():
    return "Forgot password functionality coming soon!"