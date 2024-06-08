from flask import Flask, jsonify
from flask_restful import Api
from config import Config
from database import init_db
from resources.item import ItemResource, ItemListResource
from resources.user import UserResource, UserListResource
from resources.bid import BidResource, BidListResource

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)

init_db(app)

api.add_resource(ItemListResource, '/items')
api.add_resource(ItemResource, '/items/<int:item_id>')
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(BidListResource, '/bids')
api.add_resource(BidResource, '/bids')

@app.route('/')
def home():
    return jsonify({"message": "API Leilao"})

if __name__ == '__main__':
    app.run(debug=True)
