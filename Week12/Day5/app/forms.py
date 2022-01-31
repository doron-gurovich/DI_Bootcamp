import flask_wtf
import wtforms
from wtforms import ValidationError


# wrapper function
def length(min=-1, max=-1):
	def my_length_check(form, field):
		if len(field.data) > 50:
			raise ValidationError('Field must be less than 50 characters')

	return my_length_check


class Register(flask_wtf.FlaskForm):
	username = wtforms.StringField(label="Name", validators=[length(5, 10)])
	password = wtforms.PasswordField("Password", [wtforms.validators.DataRequired()])
	bio = wtforms.StringField("Bio")
	check = wtforms.BooleanField("checkbox")
	radioFields = wtforms.RadioField(choices=["red", "green", "blue"])
	dropBox = wtforms.SelectField(choices=["red", "green", "blue"])
	fileField = wtforms.FileField()

	submit = wtforms.SubmitField("Submit")


class Details(flask_wtf.FlaskForm):
	studentID = wtforms.IntegerField(label="Student ID", validators=[wtforms.validators.DataRequired()])
	firstName = wtforms.StringField(label="First NAme", validators=[wtforms.validators.DataRequired()])
	lastName = wtforms.StringField(label="Last Name", validators=[wtforms.validators.DataRequired()])
	age = wtforms.FloatField(label="Age", validators=[wtforms.validators.DataRequired(),
													  wtforms.validators.NumberRange(min=1, max=100)])

	submit = wtforms.SubmitField("Submit")
