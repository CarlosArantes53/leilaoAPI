from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    start_bid = fields.Float(required=True)
    highest_bid = fields.Float(dump_only=True)
    end_time = fields.DateTime(required=True)
    user_id = fields.Int(required=True)
