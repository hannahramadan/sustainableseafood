# Sustainable Seafood
by Hannah Ramadan

As a vegetarian for over 8 years, I’ve gotten a lot of “you don’t even fish?” This got me thinking about the number of people who would cut down on meat consumption, while keeping fish in their diet. For my solo capstone project at [Hackbright Academy](https://hackbrightacademy.com/), I created Sustainable Seafood. 

Sustainable Seafood is a webapp where users can search for, discover, and keep track of sustainable seafood. This app aims to help people make better food choices they make when it comes to eating sustainably.

<img width="1440" alt="Screen Shot 2021-06-18 at 7 01 18 AM" src="https://user-images.githubusercontent.com/76922290/122572858-01e20100-d003-11eb-8e1b-1eaaa585b2d5.png">

## Features
- Display North American seafood species, their sustainability status, population, environmental considerations and more. (FishWatch.gov Species Content API)
- Allows users to search for species by name.
- Filter and discover new species by sustainability rating and geographic region. 
- Save species to personal watchlist.
- Users can send their watchlistlist to their phones. (Twilio API)
- See nearest farmers markets by zip code. (USDA National Farmers Market Directory API)

## Tech Stack

- Backend: Python3, Flask, PostgreSQL, SQLAlchemy, Jinja2
- Frontend: JavaScript, jQuery, HTML5, CSS, Bootstrap
- APIs: Twilio for SMS, FishWatch.gov Species Content, USDA National Farmers Market Directory


![Untitled design](https://user-images.githubusercontent.com/76922290/122577291-76b73a00-d007-11eb-839d-f5051895bf08.png)

## Installation Instructions ##
### Prerequisites ###

You will need the following API keys:

- [Twilio API](https://www.twilio.com/docs/usage/api)
- [FishWatch.gov Species Content API](https://www.fishwatch.gov/developers)
- [USDA National Farmers Market Directory API](https://search.ams.usda.gov/farmersmarkets/v1/svcdesc.html)

**Python3** and **PostgreSQL** will also need to be installed.

## Running Sustainable Seafood ##

1. Clone this repository:

``` 
git clone https://github.com/hannahramadan/sustainableseafood.git 
```

2. Optional: Create and activate a virtual environment:

``` 
pip3 install virtualenv
virtualenv env
source env/bin/activate 
```

3. Install dependencies:

``` 
pip3 install -r requirements.txt 
```

4. Create environmental variables to hold your API keys in a secrets.sh file:

```
export TWILIO_AUTH_TOKEN='{TWILIO_AUTH_TOKEN}' 

export TWILIO_ACCOUNT_SID='{TWILIO_ACCOUNT_SID}' 

export TWILIO_PHONE_NUMBER='{TWILIO_PHONE_NUMBER}' 
```

5. Create your database & seed sample data:

```
createdb sustainablefish
python3 seed.py 
```

6. Run the app on localhost:

```
source secrets.sh
python3 server.py
```
## Future Features
- Sustainability quiz
- Visualization of most watched fish

Thanks for viewing my project! Check out my [LinkedIn](https://www.linkedin.com/in/hannahramadan/) to see what I'm up to.
