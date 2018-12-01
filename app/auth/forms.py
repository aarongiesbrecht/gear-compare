from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DecimalField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class InputForm(FlaskForm):
    class_name = StringField('class', validators=[DataRequired()])
    eff = DecimalField('efficiency', places=1, validators=[DataRequired()])
    primary = StringField('primary', validators=[DataRequired()])
    secondary = StringField('secondary', validators=[DataRequired()])
    heavy = StringField('heavy', validators=[DataRequired()])
    fireteam = BooleanField('Game was with a fireteam')
    submit = SubmitField('Record Data')

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('register')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('username already taken')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('there is already an account with that email')

class EditClanForm(FlaskForm):
    clan_name = TextAreaField('clan name', validators=[Length(min=0,max=140)])
    submit = SubmitField('save')
