from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, jsonify, render_template, request
import json

db = SQLAlchemy()

fish_json = open('fish.json').read()
fish_dict = json.loads(fish_json) 

sql = """
    INSERT INTO fishes (name, url_slug, img_url, region, quote)
    VALUES (:name, :url_slug, :img_url, :region, :quote)
    """

for item in fish_dict:
    # name = item["Species Name"]
    # url_slug = item["Path"]
    # img_url = item["Species Illustration Photo"]["src"]
    # region = item["NOAA Fisheries Region"]
    # quote = item["Quote"]
    name = "Test1"
    url_slug = "Test2"
    img_url = "Test3"
    region = "Test4"
    quote = "Test5"
    score = "T6"

    db.session.execute(sql,
                    {'name': name,'url_slug': url_slug,'img_url': img_url,'region': region,'quote': quote,'score': score})
 
    # db.session.commit()