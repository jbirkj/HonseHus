# models/honsehus.py
from db import db
from datetime import datetime


class HonseHusModel(db.Model):
    __tablename__ = 'honsehus'

    id = db.Column(db.Integer, primary_key=True)
    event_state = db.Column(db.String(80))
    event_date = db.Column(db.String(6))    #yyyymmdd
    #event_time = db.Column(db.DateTime)

    def __init__(self, state):
        self.event_state = state
        self.event_date = datetime.now().strftime("%y%m%d")

    def json(self):
        return {'state': self.event_state, 
            'date': self.event_date}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_date(cls, event_date):
        return cls.query.filter_by(event_date=event_date).first()

    @classmethod
    def find_by_state(cls, event_state):
        return cls.query.filter_by(event_state=event_state).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id)
