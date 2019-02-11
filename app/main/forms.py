from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DecimalField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User, Game_info

class InputForm(FlaskForm):
    class_name = SelectField('class', choices=[('w', 'Warlock'), ('h', 'Hunter'), ('t','Titan')], validators=[DataRequired()])
    eff = DecimalField('efficiency', places= 2, validators=[DataRequired()])
    primary = SelectField('primary', choices=[('hc','Hand Cannon'), ('ar','Auto Rifle'),
        ('pr','Pulse Rifle'), ('sc','Scout Rifle'), ('bo','Bow'), ('sa','Sidearm'),
        ('sg','Shotgun'), ('sr','Sniper Rifle'), ('gl', 'Grenade Launcher')], validators=[DataRequired()])
    secondary = SelectField('secondary', choices=[('hc','Hand Cannon'), ('ar','Auto Rifle'),
        ('pr','Pulse Rifle'), ('sc','Scout Rifle'), ('bo','Bow'), ('sa','Sidearm'),
        ('sg','Shotgun'), ('gl', 'Grenade Launcher'), ('sr','Sniperifle'), ('fr','Fusion Rifle')], validators=[DataRequired()])
    heavy = SelectField('heavy', choices=[('rl', 'Rocket Launcher'),
        ('lf', 'Linear Fusion'), ('gl', 'Grenade Launcher'), ('mg', 'Machine Gun'),
        ('sr', 'Sniper Rifle'), ('sg', 'Shotgun'), ('sw', 'Sword')], validators=[DataRequired()])
    map = SelectField('map', choices=[('mid', 'Midtown'), ('ret', 'retribution'),
        ('end', 'endless vale'), ('vos', 'vostok'), ('aof', 'altar of flame'),
        ('jav', 'javelin-4'), ('tdc', 'the deac cliffs'), ('for', 'the fortress'),
        ('gul', 'legions gulch'), ('emp', 'emperor\'s respite'), ('ete', 'eternity'),
        ('dsh', 'distant shores'), ('wor', 'wormhaven'), ('pac', 'pacifica'),
        ('rad', 'radiant cliffs')], validators=[DataRequired()])
    fireteam = BooleanField('Game was with a fireteam')
    submit = SubmitField('Record Data')

class EditClanForm(FlaskForm):
    clan_name = TextAreaField('clan name', validators=[Length(min=0,max=140)])
    submit = SubmitField('save')
