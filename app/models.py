from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post = db.Column(db.String(255))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitch',lazy = "dynamic")
    category = db.Column(db.String(255))

    '''
    Pitch class to define pitch columns
    '''

    # def __init__(self, id, title, post, poster, vote_average, vote_count):
    #     self.id = id
    #     self.title = title
    #     self.post = post
    def save_pitch(self):
        
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(category_id = id).all()
        return pitches



class User(UserMixin,db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)


# class Category(db.Model):
#     __tablename__ = 'categories'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255), index = True)
#     pitches = db.relationship('Pitch',backref = 'category',lazy = "dynamic")

#     @classmethod
#     def get_categories(cls):
#         categories = Category.query.all()
#         return categories




class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey(
        'pitches.id'), nullable=False)
    time = db.Column(db.DateTime, default = datetime.utcnow)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    # def save_comment(self):


    # @classmethod
    # def get_comments(cls, id):

    # for comment in cls.all_comments:
    #     if comment.pitch_id == id:


    # def __repr__(self):


