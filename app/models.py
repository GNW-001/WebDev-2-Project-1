from . import db

class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(511))
    bedroom = db.Column(db.Integer)
    bathroom = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Float)
    type = db.Column(db.String(40))
    imageName = db.Column(db.String(80))

    def __init__(self, title, description, bedroom, bathroom, location, price, type, imageName):
        self.title = title
        self.description = description
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.location = location
        self.price = price
        self.type = type
        self.imageName = imageName

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)
