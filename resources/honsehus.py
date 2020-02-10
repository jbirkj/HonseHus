# resources/honsehus.py
from flask_restful import Resource, reqparse
from models.honsehus import HonseHusModel


class HonseHus(Resource):

    '''
    def put(self, status):
        
        EventState = HonseHusModel.find_by_state(status)
        
        if EventState:
            return EventState.json()
        
        return {'message': 'Eventstate not found'}, 400
    '''

    def get(self, Ddate):
        
        EventState = HonseHusModel.find_by_date(Ddate)
        print("here")
        if EventState:
            return EventState.json()
        
        return {'message': 'Eventstate not found'}, 400

    def post(self, status):
        
        h = HonseHusModel(status)

        try:
            h.save_to_db()
        except:
            return {"message": "An error ocurred saving to db"}, 500

        return h.json(), 201

class HH(Resource):
    def get(self):
        return {'HonseHid updates': list(map(lambda x: x.json(), HonseHusModel.query.all()))}
