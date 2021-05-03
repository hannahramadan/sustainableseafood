from flask_sqlalchemy import SQLAlchemy
import json


db = SQLAlchemy()

class User(db.Model):
    """A user belonging to Sustainable Fish."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique = True)
    password = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(50), nullable=True)
    
    def __repr__(self):
        """Provide user representation when printed."""

        return f"<User user_id={self.user_id} email={self.email}>"


class Favorite(db.Model):
    """A favorited fish."""

    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    fish_id = db.Column(db.Integer, db.ForeignKey('fishes.fish_id'))

    user = db.relationship('User', backref = "favorites") 
    fish = db.relationship('Fish', backref = "favorites")

    def __repr__(self):
        """Provide favorite representation when printed."""

        return f"<Favorite favorite_id={self.user_id} user_id={self.user_id} fish_id={self.fish_id}>"


class Fish(db.Model):
    """A fish belonging to Sustainable Fish."""

    __tablename__ = "fishes"

    fish_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), unique = True, nullable=False)
    url_slug = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)
    region = db.Column(db.String(200), nullable=False)
    score = db.Column(db.String(1), nullable=False)

    favorite = db.relationship("Favorite")
    
    def __repr__(self):
        """Provide fish representation when printed."""

        return f"<Fish fish_id={self.fish_id} name={self.name}>"

class AssociatedName(db.Model):
    """Associated names of fish Fish."""

    __tablename__ = "associated_names"

    assoc_name_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    fish_id = db.Column(db.Integer, db.ForeignKey('fishes.fish_id'))

    fish = db.relationship('Fish', backref = "associated_names")

    def __repr__(self):
        """Provide fish representation when printed."""

        return f"<Assoc Name assoc_name_id={self.assoc_name_id} name={self.name}>"


### Add fish from JSON to DB ###
fish_json = open('fish.json').read()
fish_dict = json.loads(fish_json) 

def connect_to_db(flask_app, db_uri='postgresql:///sustainablefish', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
