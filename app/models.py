from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    '''
    Pitch class to define pitch columns
    '''

    def __init__(self, id, title, post, poster, vote_average, vote_count):
        self.id = id
        self.title = title
        self.post = post


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    password_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)


class Comment:
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey(
        'pitches.id'), nullable=False)

    # def save_comment(self):


    # @classmethod
    # def get_comments(cls, id):

    # for comment in cls.all_comments:
    #     if comment.pitch_id == id:


    # def __repr__(self):


