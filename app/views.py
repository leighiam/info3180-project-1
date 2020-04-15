"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .forms import ProfileForm
from .models import UserProfile
from datetime import date

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Ashleigh Barker")


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    form = ProfileForm(request.form)

    if request.method == 'POST':
        firstname = form.fname.data
        lastname = form.lname.data
        gen = form.gender.data
        eml = form.email.data
        loc = form.location.data
        bio = form.biography.data
        propic = request.files['image']
        filename = secure_filename(propic.filename)
        propic.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))
        datecreated = get_date_joined()
        user = UserProfile(firstname, lastname, gen, eml, loc, bio, filename, datecreated) 
        db.session.add(user)
        db.session.commit()
        
        flash("Profile successfully created")
        return redirect(url_for('profiles'))
    return render_template('profile.html', form=form)


@app.route('/profiles', methods=["GET", "POST"])
def profiles():
    users = UserProfile.query.all()
    if request.method == "GET":
        return render_template('profiles.html', users=users)

@app.route('/profile/<userid>')
def getUserProfile(userid):
    user = UserProfile.query.filter_by(userid=userid).first()
    return render_template('userprofile.html', user=user)
    
    
def get_date_joined():
    today = date.today()
    date_joined = today.strftime("%B %d, %Y")
    return date_joined



###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
