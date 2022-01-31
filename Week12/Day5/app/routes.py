import json

import flask
from flask import abort

from app import app, db
from app.forms import Register, Details
from app.models import Student, Book


@app.route('/', methods=['GET'])
def index():
	return flask.render_template('index.html', new_color=False)


@app.route('/flash_mgs', methods=['GET'])
def flash_mgs():
	abort(500)
	flask.flash("Error", "error")
	flask.flash("Logged in successfully", "success")
	return flask.render_template('flash.html', new_color=False)


@app.route('/blank/<color>', methods=['GET'])
def blank(color):
	if color not in ['blue', 'red', 'green', 'yellow', 'orange', 'red']:
		abort(400)

	return flask.render_template('blank.html', color=color)


@app.route('/users/<name>', methods=['POST'])
def add_blank(name):
	with open('../examplle.json', 'r') as f:
		users = json.load(f)

	users.append({'name': name})

	with open('../examplle.json', 'w') as f:
		json.dump(users, f, indent=2)


@app.route('/myform', methods=("GET", "POST"))
def myform():
	registerForm = Register()

	if registerForm.validate_on_submit():  # Check if the form has been filled
		username = registerForm.username.data  # Get
		password = registerForm.password.data  # The
		bio = registerForm.bio.data  # Data

		print("Here is what I got from the form:")
		print("username:", username)
		print("password:", password)
		print("bio:", bio)
		# Do something with the data

		return flask.redirect('/')
	return flask.render_template("register.html", form=registerForm)


@app.route('/mydetails', methods=("GET", "POST"))
def details_form():
	_detailsForm = Details()

	if _detailsForm.validate_on_submit():
		id = _detailsForm.studentID.data
		firstName = _detailsForm.firstName.data
		lastName = _detailsForm.lastName.data
		age = _detailsForm.age.data

		new_student = Student(student_id=id, first_name=firstName, last_name=lastName, age=age)

		db.session.add(new_student)
		db.session.commit()

		return flask.redirect('/')

	return flask.render_template("details.html", form=_detailsForm)


@app.route('/create_book/<int:book_id>/<name>/<int:price>')
def create_book(book_id, name, price):
	book = Book(book_id=book_id, name=name, price=price)
	db.session.add(book)
	db.session.commit()

	return f"the book {book_id} created successfully"


@app.route('/get_books')
def get_all_books():
	all_books = Book.query.all()
	books_id = [book.name for book in all_books]
	return f"all the books at the db are: {books_id}"
