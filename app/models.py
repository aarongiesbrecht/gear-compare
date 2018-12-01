from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#database model for storing user info
class User (UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    clan_name = db.Column(db.String(140))
    games = db.relationship('Game_info', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User: {}>' .format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def all_games(self):
        return Game_info.query.order_by(Game_info.id.desc())


#database model for storing game info
class Game_info (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(64))
    eff = db.Column(db.Integer)
    fireteam = db.Column(db.Boolean)
    primary = db.Column(db.String(64))
    secondary = db.Column(db.String(64))
    heavy = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return '<Class: {}>\n<Efficiency: {}>' .format(self.class_name, self.eff)
