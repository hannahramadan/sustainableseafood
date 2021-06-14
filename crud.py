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

def delete_favorite(user_id, fish_id):
    """Delete a favorite."""
    favorite = Favorite.query.filter((Favorite.user_id == user_id)&(Favorite.fish_id==fish_id)).one()

    db.session.delete(favorite)
    db.session.commit()
    return favorite

def does_favorite_exist(user_id, fish_id):
    """Find a favorite."""
    if Favorite.query.filter((Favorite.user_id == user_id)&(Favorite.fish_id==fish_id)).count() > 0:
        return True
    else:
        return False

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

def new_zip_code(email, zip_code):
    """New user zip_code"""
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

def get_fish_name(fish_id):
    """Return a fish."""
    fish = Fish.query.get(fish_id)
    return fish.name

def get_fish_score(fish_id):
    """Return a fish."""
    fish = Fish.query.get(fish_id)
    score = fish.score
    return score

def get_fish_by_rating(score):
    """Return fish objects by rating"""
    return Fish.query.filter(Fish.score == score).all()

def get_fish_by_region(region):
    """Return fish objects by region"""
    
    fishes = get_all_fish()
    final=[]
    for fish in fishes:
        regions = fish.region
        divided = regions.split(", ")
        for item in divided:
            if item == region:
                final.append(fish)

    return final

def get_fish_by_rating_and_region(score, region):
    """Return fish objects by region"""

    final = []

    scores = get_fish_by_rating(score)
    regions = get_fish_by_region(region)

    for item in scores:
        if item in regions:
            final.append(item)

    return final

def get_all_by_rating_and_region(scores, regions):
    """Return fish objects by region"""
    
    fishes = get_all_fish()
    final=[]
    
    if scores == []:
        scores = ["1", "2", "3"]
    #if no score is selecetd, all scores are okay

    if regions == []:
    #user didn't select any regions, so all regions are okay
        for fish in fishes:
            if fish.score in scores:
                final.append(fish)
    else: #some regions were selected
        for fish in fishes:
            regions_of_fish = fish.region 
            divided = regions_of_fish.split(", ") #some fish have multiple regions, only one region satisfies search
            for item in divided: #looping so that I can check each region and the given score(s)
                if item in regions and fish.score in scores:
                    final.append(fish)
                    break #out of 2nd for loop

    return final

def fish_likes(fish_id):
    return Favorite.query.filter(Favorite.fish_id == fish_id).count()

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

def get_all_fishes_by_rating(scores):
    fishes = get_all_fish()
    final=[]
    
    if scores == []:
        return fishes
    #if no score is selecetd, all scores are okay

    for fish in fishes:
        if fish.score in scores:
            final.append(fish)

    return final

def get_all_fishes_by_region(regions):
    fishes = get_all_fish()
    final=[]
    
    if regions == []:
        return fishes

    for fish in fishes:
            regions_of_fish = fish.region 
            divided = regions_of_fish.split(", ") #some fish have multiple regions, only one region satisfies search
            for item in divided: #looping so that I can check each region and the given score(s)
                if item in regions:
                    final.append(fish)
                    break #out of 2nd for loop
    return final

def update_phone_number(phone_number, user_id):
    user = User.query.filter(User.user_id == user_id).first()
    user.phone_number = phone_number
    db.session.add(user)
    db.session.commit()
    return user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
