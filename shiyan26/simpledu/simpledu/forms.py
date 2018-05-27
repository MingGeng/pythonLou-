from flask_wtf import FlaskForm
from wtforms import StringField, PassworField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[Required(), Length(3, 24)])
    email = StringField('email', validators=[Required(), Email()])
    password = PassworField('password', validators=[Required(), Length(6, 24)])
    repeat_password = PassworField('repeat_password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('submit')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[Required(), Length(6, 24)])
    password = PassworField('password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('submit')

