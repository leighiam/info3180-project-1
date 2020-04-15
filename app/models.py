from . import db


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    userid = db.Column(db.BigInteger, db.Sequence('user_profiles_userid_seq', start=620092920, increment=1), primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(255))
    image = db.Column(db.String(255))
    date = db.Column(db.String(80))
    
    def __init__(self, first_name, last_name, gender, email, location, biography, image, date):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.image = image
        self.date = date
        

    """def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False"""

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.userid)
