from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('product','product'),('lyric','lyric'),('sales','sales'),('pick-up lines','pick-up lines'),('personal','personal')],validators=[Required()])
    post = TextAreaField('Your Pitch', validators=[Required()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment...',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')