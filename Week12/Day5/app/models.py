from app import db


class Student(db.Model):
	student_id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64))
	last_name = db.Column(db.String(64))
	age = db.Column(db.Float)

	def __repr__(self):
		return f'<Student: {self.first_name}>'


class Book(db.Model):
	book_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	price = db.Column(db.Float)

	def __str__(self):
		return f'<Book: {self.book_id}>'
