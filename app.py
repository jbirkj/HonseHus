from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from resources.honsehus import HonseHus

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('home.html')



api.add_resource(HonseHus, 
    '/date/<string:date>',
    '/status/<string:status>', 
    '/update/<string:status>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
