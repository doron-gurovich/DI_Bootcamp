import flask_wtf
import wtforms


class Login(flask_wtf.FlaskForm):
	name = wtforms.StringField(label="name", validators=[wtforms.validators.DataRequired()])
	city_name = wtforms.StringField(label="city name", validators=[wtforms.validators.DataRequired()])

	submit = wtforms.SubmitField("Submit")


class Register(flask_wtf.FlaskForm):
	name = wtforms.StringField(label="name", validators=[wtforms.validators.DataRequired()])
	city_name = wtforms.StringField(label="city name", validators=[wtforms.validators.DataRequired()])

	submit = wtforms.SubmitField("Submit")