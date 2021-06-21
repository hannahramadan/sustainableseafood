"""Server for fish app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import requests
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
from model import Fish
import json
import os
from twilio.rest import Client

app = Flask(__name__)
app.secret_key = "dev"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route('/')
def base():
    """View login page"""
    return render_template ('login.html')


@app.route('/createaccount', methods=['POST'])
def createaccount():
    """View login page"""

    email = request.form.get('email')
    password = request.form.get('password')

    email_in_use = crud.get_user_by_email(email)

    if email_in_use == None:
        user = crud.create_user(email, password, zip_code = 99999, phone_number = "null")
        session["user_email"] = user.email
        return render_template ('createaccount.html',
                                email = email,
                                password = password)
    
    else:
        flash("Email already in use")
        return redirect ("/")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    zip_code = request.form.get('zip_code')

    user = crud.get_user_by_email(email)

    if user is None:
        flash("No email found")
        return redirect ("/")
    
    elif user.password != password:
        flash("Incorrect password")
        return redirect ("/")
    
    elif user.zip_code == 99999:
        crud.update_zip_code(email,zip_code)
        return redirect ('/search')
            
    else:
        session["user_email"] = user.email
        return redirect ('/search')

@app.route('/search')
def search():  

    if (session.get('user_email')) == None:
        return redirect("/")

    fishes = crud.get_all_fish()

    fishnamelist = []

    for fish in fishes:
        fishnamedict = {}
        fishnamedict['label'] = fish.name
        fishnamedict['value'] = f'http://localhost:5000/species/{fish.fish_id}'
        fishnamedict['img'] = fish.img_url
        fishnamelist.append(fishnamedict)
    

    return render_template ('search.html', fishes=fishes, fishnamelist=fishnamelist)

    #endpoint that returns jsonified list and AJAX call to retrive


@app.route('/discover')
def all_fish():

    if (session.get('user_email')) == None:
        return redirect("/")

    # for pagination
    page = request.args.get('page', 1, type=int)
    fishes = Fish.query.paginate(page = page, per_page=12)

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    user_id = user.user_id

    favorites = crud.get_favorite_fish_by_user(user.user_id)

    return render_template("species.html", fishes=fishes, favorites=favorites)

@app.route('/species/<fish_id>')
def get_species_details(fish_id):
    """View the details of a fish."""

    if (session.get('user_email')) == None:
        return redirect("/")

    fish = crud.get_fish_by_id(fish_id)

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    user_id = user.user_id

    favorites = crud.get_favorite_fish_by_user(user.user_id)

    img = fish.img_url
    name = fish.name
    likes = crud.fish_likes(fish_id)

    url = f'https://www.fishwatch.gov/api/species/{name}'

    response = requests.get(url)
    species = response.json()

    species_name = species[0]["Species Name"]
    species_region = species[0]["NOAA Fisheries Region"]
    population_status = species[0]["Population Status"]
    population = species[0]["Population"]
    habitat_impacts = species[0]["Habitat Impacts"]
    scientific_name = species[0]["Scientific Name"]
    fishery_management = species[0]["Fishery Management"]
    score = crud.get_fish_score(fish_id)

    return render_template('species_details.html', 
                           fish=fish,
                           favorites=favorites,
                           species_name=species_name,
                           species_region=species_region,
                           population_status=population_status,
                           population=population,
                           habitat_impacts=habitat_impacts, 
                           likes=likes,
                           score=score,
                           img=img, 
                           scientific_name=scientific_name,
                           fishery_management=fishery_management)

@app.route('/profile')
def show_user():
    """Show particular user's profile page."""
    if (session.get('user_email')) == None:
        return redirect("/")

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    favorites = crud.get_favorite_fish_by_user(user.user_id)

    return render_template('profile.html', user = user)

@app.route('/watchlist')
def watchlist():
    """Show particular user's watchlist."""
    if (session.get('user_email')) == None:
        return redirect("/")

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    favorites = crud.get_favorite_fish_by_user(user.user_id)

    return render_template('watchlist.html', user = user, favorites=favorites)

@app.route('/shoplocal')
def shop_local():
    """Show particular user's profile page."""
    if (session.get('user_email')) == None:
        return redirect("/")

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)

    return render_template('shoplocal.html', user = user)

@app.route('/logout')
def log_out():
    """Log out."""
    session.clear()

    return redirect('/')

@app.route('/favorite_fish/<fish_id>', methods=['POST'])
def favorite(fish_id):
    """Favorite or remove a fish."""
    if (session.get('user_email')) == None:
        return redirect("/")

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    user_id = user.user_id

    if crud.does_favorite_exist(user_id, fish_id) == True:
        crud.delete_favorite(user_id, fish_id)
        response = "Add to watchlist"
    else:
        crud.create_favorite(user_id, fish_id)
        response = "Remove from watchlist"

    return jsonify(response)

@app.route('/search_results')
def search_fish():
    """Seach results."""

    if (session.get('user_email')) == None:
        return redirect("/")
    
    ratings = request.args.getlist('rating')
    regions = request.args.getlist('region')

    fishes_with_correct_rating = crud.get_all_fishes_by_rating(ratings)
    fishes_with_correct_region = crud.get_all_fishes_by_region(regions)

    fishes = []

    for fish in fishes_with_correct_rating:
        if fish in fishes_with_correct_region:
            fishes.append(fish)

    return render_template ('/search_results.html',
                            fishes=fishes,
                            ratings=ratings, 
                            regions=regions)


@app.route('/updatezipcode', methods=['POST'])
def updatezipcode():
    """Update user zip code."""
    if (session.get('user_email')) == None:
        return redirect("/")

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    favorites = crud.get_favorite_fish_by_user(user.user_id)
    
    zip_code = request.form.get('zip_code')

    crud.new_zip_code(user_email, zip_code)

    return redirect("/shoplocal") 

@app.route('/species/favorite_fish/<fish_id>', methods=['POST'])
def detailfavorite(fish_id):
    """Favorite or remove a fish."""
    if (session.get('user_email')) == None:
        return redirect("/")

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    user_id = user.user_id

    if crud.does_favorite_exist(user_id, fish_id) == True:
        crud.delete_favorite(user_id, fish_id)
        response = "Add to watchlist"
    else:
        crud.create_favorite(user_id, fish_id)
        response = "Remove from watchlist"

    return jsonify(response)

## React Practice ##
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/play")
def play():
    return render_template("play.html")

@app.route('/text_fish', methods=["POST"])
def text_fish():

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    user_id = user.user_id

    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    favorites = crud.get_favorite_fish_by_user(user.user_id)

    crud.update_phone_number(phone_number, user_id)

    text_list = []

    for fish in favorites:
        text_list.append(fish.name +": "+fish.score+ "\n")

    msg = ''.join(text_list)

    message = client.messages \
                    .create(
                        body=msg,
                        from_='+15072003197',
                        # would change phone number if live, can only send to verified Twilio number
                        to='+15599993054'
                    )
    return redirect(request.referrer)

@app.route("/species")
def species_redirect():
    return redirect("/discover")

@app.route("/aboutme")
def aboutme():
    return render_template ("/aboutme.html")

### Option using one function at a time ###
    # ratings = request.args.getlist('rating')
    # regions = request.args.getlist('region')

    # fishes = crud.get_all_by_rating_and_region(ratings, regions)
    
    # # return render_template ('/search_results')
    # return render_template ('/search_results.html',
    #                 fishes=fishes)

###########################################

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)