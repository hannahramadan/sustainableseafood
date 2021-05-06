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
    print(zip_code)
    print("**********************")

    user = crud.get_user_by_email(email)

    if user is None:
        flash("No email found")
        return redirect ("/")
    
    elif user.password != password:
        flash("Incorrect password")
        return redirect ("/")
    
    elif user.zip_code == 99999:
        crud.update_zip_code(email,zip_code)
        return redirect ('/homepage')
            
    else:
        session["user_email"] = user.email
        return redirect ('/homepage')

@app.route('/homepage')
def homepage():
    return render_template ('homepage.html')


@app.route('/species')
def all_fish():
    fishes = crud.get_all_fish()

    return render_template("species.html", fishes=fishes)

@app.route('/species/<fish_id>')
def get_species_details(fish_id):
    """View the details of a fish."""

    fish = crud.get_fish_by_id(fish_id)
    name = fish.name

    url = f'https://www.fishwatch.gov/api/species/{name}'

    response = requests.get(url)
    species = response.json()

    species_name = species[0]["Species Name"]
    species_region = species[0]["NOAA Fisheries Region"]
    population_status = species[0]["Population Status"]
    population = species[0]["Population"]
    habitat_impacts = species[0]["Habitat Impacts"]

    return render_template('species_details.html',
                           species_name=species_name,
                           species_region=species_region,
                           population_status=population_status,
                           population=population,
                           habitat_impacts=habitat_impacts)

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


##########################################################################

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



# Replace this with routes and view functions!

# @app.route('/movies')
# def all_movies():

#     movies = crud.get_movies()

#     return render_template('all_movies.html',
#                             movies = movies)

# @app.route('/movies/<movie_id>')
# def show_movie(movie_id):
#     """Show details on a particular movie."""
#     movie = crud.get_movie_by_id(movie_id)

#     return render_template('movie_details.html', movie = movie) 

# @app.route('/users')
# def all_users():

#     users = crud.get_users()

#     return render_template('all_users.html',
#                             users = users)


# @app.route('/users/<user_id>')
# def show_user(user_id):
#     """Show details on a particular user."""
#     user = crud.get_user_by_id(user_id)

#     return render_template('user_details.html', user = user) 


# @app.route('/user', methods = ['POST'])
# def register_user():
#     """Create a new user."""

#     email = request.form.get("email")
#     password = request.form.get("password")

#     user = crud.get_user_by_email(email)
#     if user:
#         flash('Cannot create an account with that email. Try again.')
#     else:
#         crud.create_user(email, password)
#         flash('Account created! Please log in.')

#     return redirect('/')


# @app.route('/check_if_account')
# def check_if_account():
#     """check to see if user in db"""

#     email = request.args.get("login_email")
#     password = request.args.get("login_password")

#     Session = sessionmaker(bind=engine)
#     s = Session()
#     query = s.query(Users).filter(Users.email.in_([email]), Users.password.in_([password]) )
#     result = query.first()
#     if result:
#         flash ('logged In')
#     else:
#         flash('wrong password!')

    # if User.query.filter_by(email = 'email') == email:
    #     if db.session.query(User.email, User.password).one() == (email,password):
    #         flash('Logged In')
    #         return redirect('/')
    #     else:
    #         flash('Password incorrect')
    # else:
    #     flash('Create an account')

# if user id matches with email in db && password = password-> flash "logged in"
# else flash -> "user not found"

# email -> check if email is associated with user id
# Y -> if email matches password

# username = request.form['username'] </form>
# password = request.form['password']
# if password == 'let-me-in': # FIXME
# session['current_user'] = username flash(f'Logged in as {username}') return redirect('/')
# else:
# flash('Wrong password!') return redirect('/login')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
