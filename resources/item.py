from flask_restful import Resource, reqparse
from models import Item, db
from schemas.item_schema import ItemSchema
from flask import request
from datetime import datetime, timedelta

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class ItemResource(Resource):
    def get(self, item_id=None):
        if item_id:
            item = Item.query.get_or_404(item_id)
            return item_schema.dump(item)
        else:
            items = Item.query.all()
            return items_schema.dump(items)

    def post(self):
        data = request.get_json()
        item = item_schema.load(data)
        db.session.add(item)
        db.session.commit()
        return item_schema.dump(item), 201

class ItemListResource(Resource):
    def get(self):
        items = Item.query.all()
        return items_schema.dump(items)
