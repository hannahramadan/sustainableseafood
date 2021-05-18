"""Server for fish app."""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
import requests
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
from model import Fish

app = Flask(__name__)
app.secret_key = "dev"


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
    fishes = crud.get_all_fish()
    return render_template ('search.html', fishes=fishes)

@app.route('/species')
def all_fish():
    fishes = crud.get_all_fish()

    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    user_id = user.user_id

    # # could only check for fish in favorites and return "remove", else return "add"

    favorites = crud.get_favorite_fish_by_user(user.user_id)

    # # for fish in favorites:
    # #     fish_id = get_fish_by_id(fish.fish_id)

    # for fish in favorites:
    #     watchlist = "Remove from watchlist"

    #     else:
    #         watchlist = "Add to watchlist"


    # for fish in fishes:
    #     if crud.does_favorite_exist(user_id, fish.fish_id) == True:
    #         watchlist = "Remove from watchlist"

    #     else:
    #         watchlist = "Add to watchlist"

    return render_template("species.html", fishes=fishes, favorites=favorites)

@app.route('/species/<fish_id>')
def get_species_details(fish_id):
    """View the details of a fish."""

    fish = crud.get_fish_by_id(fish_id)
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
    score = crud.get_fish_score(fish_id)

    return render_template('species_details.html',
                           fish=fish,
                           species_name=species_name,
                           species_region=species_region,
                           population_status=population_status,
                           population=population,
                           habitat_impacts=habitat_impacts, 
                           likes=likes,
                           score=score,
                           img=img)

@app.route('/profile')
def show_user():
    """Show particular user's profile page."""
    user_email = session["user_email"]
    user = crud.get_user_by_email(user_email)
    favorites = crud.get_favorite_fish_by_user(user.user_id)

    return render_template('profile.html', user = user, favorites=favorites)

@app.route('/logout')
def log_out():
    """Log out."""
    session.clear()

    return redirect('/')

@app.route('/favorite_fish/<fish_id>', methods=['POST'])
def favorite(fish_id):
    """Favorite or remove a fish."""

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
    ratings = request.args.getlist('rating')
    regions = request.args.getlist('region')

    fishes_with_correct_rating = crud.get_all_fishes_by_rating(ratings)
    fishes_with_correct_region = crud.get_all_fishes_by_region(regions)

    fishes = []

    for fish in fishes_with_correct_rating:
        if fish in fishes_with_correct_region:
            fishes.append(fish)

    return render_template ('/search_results.html',
                            fishes=fishes)

#################Option using one function#############################
    # ratings = request.args.getlist('rating')
    # regions = request.args.getlist('region')

    # fishes = crud.get_all_by_rating_and_region(ratings, regions)
    
    # # return render_template ('/search_results')
    # return render_template ('/search_results.html',
    #                 fishes=fishes)

########################################################################

@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/livesearch", methods=["POST", "GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "select fish from fishes where fish LIKE '{}%' order by fish".format(searchbox)
    result = cursor.fetchall()
    return jsonify(result)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
