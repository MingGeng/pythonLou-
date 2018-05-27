from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required

class RegisterForm(FlaskForm):
    username = StringField('reg_username', validators=[Required(), Length(3, 24)])
    email = StringField('reg_email', validators=[Required(), Email(message='Please input currect email address!')])
    password = PasswordField('reg_password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('reg_repeat_password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('reg_submit')

class LoginForm(FlaskForm):
    email = StringField('login_email', validators=[Required(), Email(message='Please input currect email address!')])
    password = PasswordField('login_password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('login_remember_me')
    submit = SubmitField('login_submit')

