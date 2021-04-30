"""Server for fish app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def login():
    """View login page"""

    return render_template ('login.html')

@app.route('/createaccount', methods=['POST'])
def createaccount():
    """View login page"""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.create_user(email, password, zip_code = "null", phone_number = "null")
    session["user_email"] = user.email

    return render_template ('createaccount.html',
                            email = email,
                            password = password)

@app.route('/homepage', methods=['POST'])
def homepage():
    # import pdb; pdb.set_trace()
    email = request.form.get('email')
    password = request.form.get('password')
    zip_code = request.form.get('zip_code')

    user = crud.get_user_by_email(email)

    if user.zip_code == "null":
        crud.update_zip_code(email,zip_code)
        return render_template ('homepage.html')
    
    if user is None:
        flash("No email found")
        return redirect ("/")
        
    elif user.password != password:
        flash("Incorrect password")
        return redirect ("/")
    else:
        session["user_email"] = user.email
        return render_template ('homepage.html')















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
