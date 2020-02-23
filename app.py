#app.py
import os

from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from resources.honsehus import HonseHus, HH
from models.honsehus import HonseHusModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


''' moved to run.py
@app.before_first_request
def create_tables():
    db.create_all()
'''

@app.route('/')
def index():

    return render_template('home.html')


api.add_resource(HonseHus, 
    '/getstatusbydate/<string:Ddate>', 
    '/update/<string:status>')
api.add_resource(HH, '/alldata')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
