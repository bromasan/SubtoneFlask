from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms import ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    password = PasswordField('password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('password2', validators=[DataRequired()])


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('Username', validators=[DataRequired(), Length(1, 32)])
    password = PasswordField('Password', validators=[DataRequired()])
