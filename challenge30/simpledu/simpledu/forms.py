from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required, Regexp
from simpledu.models import db, User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3, 24), Regexp('^[A-Za-z0-9]*$', 0, 'Username must have only letters,  numbers!')])
    email = StringField('Email:', validators=[Required(), Email(message='Please input currect email address!')])
    password = PasswordField('Password:', validators=[Required(), Length(6, 24, message='Password Length need to between 6 to 24!')])
    repeat_password = PasswordField('Repeat Password:', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Submit')
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exist!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exist!')


class LoginForm(FlaskForm):
    # email = StringField('Email', validators=[Required(), Email(message='Please input currect email address!')])
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remember')
    submit = SubmitField('Submit')
    # def validate_email(self, field):
    #     if field.data and not User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email unregistered!')
    def validate_username(self, field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidationError('User unregistered!')

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Wrong password!')
