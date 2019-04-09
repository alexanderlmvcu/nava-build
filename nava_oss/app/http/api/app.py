from flask import Flask, json, g, request
from nava_oss.app.wave.service import Service as Wave
from nava_oss.app.wave.schema import RaspberryPiSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/waves", methods=["GET"])
def index():
 return json_response(Wave(g.user).find_all_waves())


@app.route("/waves", methods=["POST"])
def create():
   raspberrySensor = RaspberryPiSchema().load(json.loads(request.data))
  
   if raspberrySensor.errors:
     return json_response({'error': raspberrySensor.errors}, 422)

   wave = Wave(g.user).create_wave_for(raspberrySensor)
   return json_response(wave)


@app.route("/wave/<int:repo_id>", methods=["GET"])
def show(repo_id):
 wave = Wave(g.user).find_wave(repo_id)

 if wave:
   return json_response(wave)
 else:
   return json_response({'error': 'wave not found'}, 404)


@app.route("/wave/<int:repo_id>", methods=["PUT"])
def update(repo_id):
   raspberrySensor = RaspberryPiSchema().load(json.loads(request.data))
  
   if raspberrySensor.errors:
     return json_response({'error': raspberrySensor.errors}, 422)

   wave_service = Wave(g.user)
   if wave_service.update_wave_with(repo_id, raspberrySensor):
     return json_response(raspberrySensor.data)
   else:
     return json_response({'error': 'wave not found'}, 404)

  
@app.route("/wave/<int:repo_id>", methods=["DELETE"])
def delete(repo_id):
 wave_service = Wave(g.user)
 if wave_service.delete_wave_for(repo_id):
   return json_response({})
 else:
   return json_response({'error': 'wave not found'}, 404)


def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})