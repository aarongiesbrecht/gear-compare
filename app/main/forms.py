from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DecimalField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User, Game_info

class InputForm(FlaskForm):
    class_name = StringField('class', validators=[DataRequired()])
    eff = DecimalField('efficiency', places= 2, validators=[DataRequired()])
    primary = StringField('primary', validators=[DataRequired()])
    secondary = StringField('secondary', validators=[DataRequired()])
    heavy = StringField('heavy', validators=[DataRequired()])
    fireteam = BooleanField('Game was with a fireteam')
    submit = SubmitField('Record Data')

class EditClanForm(FlaskForm):
    clan_name = TextAreaField('clan name', validators=[Length(min=0,max=140)])
    submit = SubmitField('save')
