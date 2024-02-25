from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from src.db import db, Station, ma



bp = Blueprint("station", __name__)


class StationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "identificacion", "emplazamiento", "servicio", "frecuencia", "unidad", "claseEmision",
                   "irradiante", "polarizacion", "cantidad", "altura", "tipoVinculo", "frecuenciaVinc",
                     "unidadVinc", "irradianteVinc", "polarizacionVinc", "provincia", "localidad",
                       "domicilio", "latitud", "longitud", "observaciones")

station_schema = StationSchema()
stations_schema = StationSchema(many=True)

@bp.route('/station/<id>', methods = ['GET'])
def get_station(id):
    try:
        # import pdb; pdb.set_trace()
        station = Station.query.get(id)
        return station_schema.dump(station)
    except:
        response = {"message": "input error"}
        return response, 400
    
@bp.route("/station/", methods = ['GET'])
def get_all_stations():
    try:
        all_stations = Station.query.all()
        # import pdb; pdb.set_trace()
        return stations_schema.dump(all_stations)
    except:
        response = {"message": "server error"}
        return response, 500


# @bp.route("/station", methods = ['POST'])
# def station():
#     try:
#         # import pdb; pdb.set_trace()

#         identificacion = request.json.get('identificacion')
#         emplazamiento = request.json.get('emplazamiento')
#         servicio = request.json.get('servicio')
#         frecuencia = request.json.get('frecuencia')
#         unidad = request.json.get('unidad')
#         claseEmision = request.json.get('claseEmision')
#         irradiante = request.json.get('irradiante')
#         polarizacion = request.json.get('polarizacion')
#         cantidad = request.json.get('cantidad')
#         altura = request.json.get('altura')
#         tipoVinculo = request.json.get('tipoVinculo')
#         frecuenciaVinc = request.json.get('frecuenciaVinc')
#         unidadVinc = request.json.get('unidadVinc')
#         irradianteVinc = request.json.get('irradianteVinc')
#         polarizacionVinc = request.json.get('polarizacionVinc')
#         provincia = request.json.get('provincia')
#         localidad = request.json.get('localidad')
#         domicilio = request.json.get('domicilio')
#         latitud = request.json.get('latitud')
#         longitud = request.json.get('longitud')
#         observaciones = request.json.get('observaciones')
#         # id_location = request.json.get('id_location')
        
#         station = Station(identificacion = identificacion, emplazamiento = emplazamiento, servicio = servicio, frecuencia = frecuencia, unidad = unidad, claseEmision = claseEmision, irradiante = irradiante, polarizacion = polarizacion, cantidad = cantidad, altura = altura, tipoVinculo = tipoVinculo, frecuenciaVinc = frecuenciaVinc, unidadVinc = unidadVinc, irradianteVinc = irradianteVinc, polarizacionVinc = polarizacionVinc, provincia = provincia, localidad = localidad, domicilio = domicilio, latitud = latitud, longitud = longitud, observaciones = observaciones)
        
#         r = db.session.add(station)
#         db.session.commit()
#         response = {"id": station.id }

#         return response, 201 
#     except Exception as e:
#         # import pdb; pdb.set_trace()

#         response = {"message": e._message()}
#         return response, 400