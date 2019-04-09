from marshmallow import Schema, fields

class RaspberryPiSchema(Schema):
    id = fields.Int(required=True)
    sensor_data = fields.Str()
    timestamp = fields.DateTime()
class WaveformSchema(RaspberryPiSchema):
    vid_id = fields.Int(required=True)
