from marshmallow import Schema, fields

class CustomerSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)

class TransactionCategorySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)

class TransactionSchema(Schema):
    id = fields.Int(required=True)
    amount = fields.Float(required=True)
    date = fields.Date(required=True)
    category_id = fields.Int(required=True)
    customer_id = fields.Int(required=True)

class SystemLogSchema(Schema):
    id = fields.Int(required=True)
    action = fields.Str(required=True)
    timestamp = fields.DateTime(required=True)
    details = fields.Str(required=True)