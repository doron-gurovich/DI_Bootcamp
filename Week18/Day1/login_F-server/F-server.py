from flask import Flask, render_template, request, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import (Form, BooleanField, StringField, SubmitField,
                    PasswordField, RadioField, validators,
                    SelectField, TextAreaField)

from wtforms.fields.html5 import EmailField

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    position = RadioField('Please define your position:',
                            choices=[('Client', 'Client'), ('Technician', 'Technician'), ('Admin', 'Admin')])
    name = StringField("Please introduce yourself: what is your name? ", validators=[DataRequired()])
    email = EmailField('Email address ', validators=[DataRequired()])

    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = InfoForm()
    if form.validate_on_submit():
        session['position'] = form.position.data
        session['name'] = form.name.data
        session['email'] = form.email.data

        return redirect(url_for('thank_u'))

    return render_template('sign-up.html', form=form)

@app.route('/thank-u')
def thank_u():
    return render_template('thank-u.html')

@app.route('/add-dish')
def add_dish():
    return render_template('add-dish.html')

@app.route('/execute-order')
def order():
    return render_template('execute-order.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/introduce-order')
def introduce_order():
    return render_template('introduce-order.html')

@app.route('/make-order')
def make_order():
    return render_template('make-order.html')

@app.route('/share-lib')
def share_lib():
    return render_template('share-lib.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
