
# Sustainable Seafood
by Hannah Ramadan

Sustainable Seafood is a webapp where users can search for, discover, and save sustinable fish in their area. This app aims to encourage people to think about the food choices they make when it comes to eating sustainably. 

### Features
- Uses FishWatch API to display North America seafood species, their sustainability status, population, environmental considerations and impact. 
- Allows users to search for species by name, and discover specieis by sustainability rating and geographic region. 
- Users can save species they are interestes in to their own watchlist.
- Users can text their watchlist list to themselves. This feature utilizes Twilio's API SMS services. 
- One of the most sustainable ways to shop is locally. On Sustainable Fish, users see their nearest farmers markets by zip code. This feature utilizes the USDA National Farmers Market Directory API. 

### Tech Stack

- Frontend: JavaScript, jQuery, HTML5, CSS, Bootstrap
- Backend: Python3, Flask, PostgreSQL, SQLAlchemy, Jinja2
- APIs: Twilio, FishWatch, USDA National Farmers Market Directory


### Running Sustainable Seafood

Clone this repository:

` git clone https://github.com/hannahramadan/sustainableseafood.git `

Optional: Create and activate a virtual environment:

` pip3 install virtualenv
virtualenv env
source env/bin/activate `

Install dependencies:

` pip3 install -r requirements.txt `

Create environmental variables to hold your API keys in a secrets.sh file:

`export TWILIO_AUTH_TOKEN='{TWILIO_AUTH_TOKEN}' `

` export TWILIO_ACCOUNT_SID='{TWILIO_ACCOUNT_SID}' `

`export TWILIO_PHONE_NUMBER='{TWILIO_PHONE_NUMBER}' `

Create your database & seed sample data:

 `createdb sustainablefish
python3 seed.py `

Run the app on localhost:

`source secrets.sh`

`python3 server.py`
