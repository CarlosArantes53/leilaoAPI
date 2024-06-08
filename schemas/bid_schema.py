from marshmallow import Schema, fields

class BidSchema(Schema):
    id = fields.Int(dump_only=True)
    amount = fields.Float(required=True)
    user_id = fields.Int(required=True)
    item_id = fields.Int(required=True)
    timestamp = fields.DateTime(dump_only=True)
