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
model.db.create_all() #creating all tabels 

with open('fish.json') as f:  #opening json file 
    fish_data = json.loads(f.read()) #adding the whole thing to fish data - loading reader

# Create fish, store them in list. Used to create fake likes later. 
fishes_in_db = []
for fish in fish_data:
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

#crud.create_fish putting it in the db

for n in range(25): #create 25 fake users
    email = f'user{n}@test.com' 
    password = 'test'
    zip_code = f'{n}'
    phone_number = f'{n}'

    user = crud.create_user(email, password, zip_code, phone_number)

for n in range(100): #create 100 fake favorites
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