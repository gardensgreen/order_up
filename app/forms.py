from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField("Employee number", {DataRequired()})
    password = PasswordField("Password", {DataRequired()})
    submit = SubmitField("Login")
