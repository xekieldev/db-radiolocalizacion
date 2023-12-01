from flask import Blueprint
from flask import flash
# from flask import g
# from flask import redirect
# from flask import render_template
# from flask import request
# from flask import url_for
# from werkzeug.exceptions import abort
# # from src.db import db, Location, ma



# bp = Blueprint("location", __name__)


# class LocationSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ("provincia", "localidad", "domicilio", "latitud", "longitud", "observaciones")

# location_schema = LocationSchema()
# locations_schema = LocationSchema(many=True)

# @bp.route('/location/<id>', methods = ['GET'])
# def get_location(id):
#     try:
#         # import pdb; pdb.set_trace()
#         location = Location.query.get(id)
#         return location_schema.jsonify(location)
#     except:
#         response = {"message": "input error en GET"}
#         return response, 400

# @bp.route("/location", methods=["POST"])
# def location():
#     try:
#         provincia = request.json.get('provincia')
#         localidad = request.json.get('localidad')
#         domicilio = request.json.get('domicilio')
#         latitud = request.json.get('latitud')
#         longitud = request.json.get('longitud')
#         observaciones = request.json.get('observaciones')
#         location = Location(provincia = provincia, localidad = localidad, domicilio = domicilio, latitud = latitud, longitud = longitud, observaciones = observaciones)
#         r = db.session.add(location)
#         db.session.commit()
#         response = {"id": location.id }
#         # import pdb; pdb.set_trace()

#         return response, 201 
#     except:
#         response = {"message": "input error"}
#         return response, 400



