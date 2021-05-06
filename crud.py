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

def get_user_by_email(email):
    """Return a user by email."""
    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user."""
    return User.query.get(user_id)

def update_zip_code(email, zip_code):
    """Update user zip_code"""
    user = User.query.filter(User.email == email).first()
    user.zip_code = zip_code
    db.session.add(user)
    db.session.commit()
    return user

def get_all_fish():
    """Return all fish."""
    return Fish.query.all()

def get_fish_by_id(fish_id):
    """Return a fish."""
    return Fish.query.get(fish_id)

def get_fish_by_rating(score):
    """Return fish objects by rating"""
    return Fish.query.filter(Fish.score == score).all()

def get_favorite_fish_by_user(user_id):
    """Get fish objects liked by a user"""
    favorites = Favorite.query.filter(Favorite.user_id == user_id).all()
    fish_ids = []
    fish_objects = []
    for item in favorites:
        fish_ids.append(item.fish_id)
    for fish in fish_ids:
        result = get_fish_by_id(fish)
        fish_objects.append(result)
    return fish_objects

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
