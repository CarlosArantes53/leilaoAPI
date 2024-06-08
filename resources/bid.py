from flask_restful import Resource, reqparse
from models import Bid, Item, db
from schemas.bid_schema import BidSchema
from flask import request

bid_schema = BidSchema()
bids_schema = BidSchema(many=True)

class BidResource(Resource):
    def post(self):
        data = request.get_json()
        bid = bid_schema.load(data)
        
        item = Item.query.get(bid.item_id)
        if bid.amount <= item.highest_bid:
            return {"message": "Bid must be higher than the current highest bid."}, 400
        
        item.highest_bid = bid.amount
        db.session.add(bid)
        db.session.commit()
        return bid_schema.dump(bid), 201

class BidListResource(Resource):
    def get(self):
        bids = Bid.query.all()
        return bids_schema.dump(bids)
