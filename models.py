from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db,login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import current_user, login_user, logout_user, login_required


class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  posts = db.relationship('Post', backref='author', lazy='dynamic')
  
  def __repr__(self):
    return '<User {}>'.format(self.username)
  
  def set_password(self,password):
    self.password_hash = generate_password_hash(password)

  def check_password_hash(self,password):
    return check_password_hash(self.password_hash, password)
  

@login.user_loader
def load_user(id):
  return User.query.get(int(id))


class Post():
  id = db.Column(db.Integer, primary_key=True)
  city = db.Column(db.String(140))
  country = db.Column(db.String(140))
  description = db.Column(db.String(140))
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '<Post {}>'.format(self.description)