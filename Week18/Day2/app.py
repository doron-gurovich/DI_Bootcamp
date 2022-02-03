from POI_project import app, db
from flask import Flask, render_template, request, redirect, session, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import (Form, BooleanField, StringField, SubmitField,
                    PasswordField, RadioField, validators,
                    SelectField, TextAreaField)

from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from POI_project.models import User
from POI_project.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in Successfully!")

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome')

            return redirect(next)

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("We are good! Thank you for the registration!")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You logged out. Thank you and see you soon!")
    return render_template(url_for('home.html'))

@app.route('/add-dish')
@login_required
def add_dish():
    return render_template('add-dish.html')

@app.route('/execute-order')
@login_required
def order():
    return render_template('execute-order.html')

@app.route('/history')
@login_required
def history():
    return render_template('history.html')

@app.route('/introduce-order')
@login_required
def introduce_order():
    return render_template('introduce-order.html')

@app.route('/make-order')
@login_required
def make_order():
    return render_template('make-order.html')

@app.route('/share-lib')
@login_required
def share_lib():
    return render_template('share-lib.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
