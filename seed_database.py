"""Script to seed database."""

import os
import json
from random import choice, randint
from model import db, User, Fish
from  sqlalchemy.sql.expression import func
import re

import crud
import model
import server

os.system('dropdb sustainablefish')
os.system('createdb sustainablefish')

model.connect_to_db(server.app) 
model.db.create_all() 

with open('fish.json') as f:  
    fish_data = json.loads(f.read()) 

 
fishes_in_db = []
for fish in fish_data:
    """Create fish and add to database"""
    name, url_slug, img_url, region, score = (fish["Species Name"],
                                        fish['Path'],
                                        fish["Species Illustration Photo"]["src"],
                                        fish["NOAA Fisheries Region"],
                                        fish["Score"]
                                        )
    db_fish = crud.create_fish(name,
                                url_slug, 
                                img_url, 
                                region,
                                score)
    fishes_in_db.append(db_fish)


for n in range(500): 
    """Create fake users"""
    email = f'user{n}@test.com' 
    password = 'test'
    zip_code = randint(5, 99999)
    phone_number = randint(10, 9999999999)

    user = crud.create_user(email, password, zip_code, phone_number)

for n in range(2000):
    """Create fake user favorites"""
    user = choice(User.query.all())
    user_id = user.user_id
    fish = choice(Fish.query.all())
    fish_id = fish.fish_id

    favorite = crud.create_favorite(user_id, fish_id)

# for fish in fish_data:
#     for name in fish["Species Aliases"]:
#         remove_ahref = re.sub("<a href.*?>", "", name)
#         remove_atag = re.sub("<..a>", "", remove_ahref)
#         x = remove_atag.split(", ")
#         print(x)
    #     for item in x:
    #         name[x] = x 
    # print(fish_data)