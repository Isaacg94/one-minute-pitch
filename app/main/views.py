from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment, User, Pitch
from .forms import CommentForm,UpdateProfile, PitchForm
from flask_login import login_required, current_user
from .. import db,photos


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Pitch | Space'
    pitches = Pitch.query.all()
    products = Pitch.query.filter_by(category = 'product').all()
    lyrics = Pitch.query.filter_by(category = 'lyric').all()
    sales = Pitch.query.filter_by(category = 'sales').all()
    lines = Pitch.query.filter_by(category = 'pick-up lines').all()
    personal = Pitch.query.filter_by(category = 'personal').all()

    return render_template('index.html',title = title, pitches = pitches, products= products, lyrics=lyrics, sales=sales, lines=lines,personal=personal  )


@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
   
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data

        

        new_pitch = Pitch(title=title, post=post, category=category, user_id=current_user.id)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', pitch_form = form)


@main.route('/user/<uname>')
def profile(uname):

    '''
    View profile page function that returns the profile details page and its data
    '''
    title = 'My Profile'
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile.html', user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('main.new_comment.html', comment_form =comment_form, pitch = pitch,all_comments=all_comments)