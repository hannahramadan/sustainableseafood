"""CRUD operations."""
import json
from model import db, User, Favorite, Fish, AssociatedName, connect_to_db

#Maybe go back: Cache stuff, call API over certain time periods, etc. 

def create_user(email, password, zip_code, phone_number):
    """Create and return a new user."""

    user = User(email= email, 
                password= password, 
                zip_code=zip_code, 
                phone_number=phone_number)

    db.session.add(user)
    db.session.commit()

    return user

def create_fish(name, url_slug, img_url, region, score):
    """Create and return a new fish."""

    fish = Fish(name = name, 
                url_slug = url_slug, 
                img_url = img_url,
                region=region, 
                score=score)

    db.session.add(fish)
    db.session.commit()

    return fish

def create_favorite(user_id, fish_id):
    """Create and return a new favorite."""

    favorite = Favorite(user_id = user_id, 
                fish_id = fish_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite

def create_alias(user_id, fish_id):
    """Create and return a new favorite."""

    favorite = Favorite(user_id = user_id, 
                fish_id = fish_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite

def get_fish():
    """Return all fish."""

    return Fish.query.all()

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()




    
#transactions grouping sequence of things happening to db line 36
# def create_rating(user, movie, score):
#     """Create and return a new rating."""

#     rating = Rating(user=user, movie=movie, score=score)

#     db.session.add(rating)
#     db.session.commit()

#     return rating

# def get_movie_by_id(movie_id):
#     return Movie.query.get(movie_id)

# def get_users():
#     """Return all users."""

#     return User.query.all()

# def get_user_by_id(user_id):
#     """Return a user."""

#     return User.query.get(user_id)

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
