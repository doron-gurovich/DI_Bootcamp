from flask import Flask, render_template, request, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, SubmitField

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):

    position = StringField("What position you hold?")
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    position = False
    form = InfoForm()
    if form.validate_on_submit():
        position = form.position.data
        form.position.data = ''

    return render_template('sign-up.html', form=form, position=position)

@app.route('/thank-u')
def thank_u():
    first = request.args.get('first')
    return render_template('thank-u.html', first=first)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
