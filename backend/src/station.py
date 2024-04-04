from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from src.db import db, Station, ma, User, Filex
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from src.users import auth, verify_password




bp = Blueprint("station", __name__)
# auth = HTTPBasicAuth()
# users = {
#     "admin": generate_password_hash("admin")
# }

# @auth.verify_password
# def verify_password(username, password):
#     # import pdb; pdb.set_trace()
#     if username in users and \
#         check_password_hash(users.get(username), password):
#         return username




class StationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "status2", "identificacion", "emplazamiento", "servicio", "frecuencia", "unidad", "claseEmision",
                   "irradiante", "polarizacion", "cantidad", "altura", "tipoVinculo", "frecuenciaVinc",
                     "unidadVinc", "irradianteVinc", "polarizacionVinc", "provincia", "localidad",
                       "domicilio", "latitud", "longitud", "observaciones")

station_schema = StationSchema()
stations_schema = StationSchema(many=True)

@bp.route('/station/<id>', methods = ['GET'])
@auth.login_required
def get_station(id):
    try:
        # import pdb; pdb.set_trace()
        station = Station.query.get(id)
        return station_schema.dump(station)
    except:
        response = {"message": "input error"}
        return response, 400
    
@bp.route("/station", methods = ['GET'])
@auth.login_required
def get_all_stations():

    try:
        include_deleted = request.args.get('includeDeleted')
        usuario = auth.current_user()
        checkUser= User.query.filter_by(usuario=usuario).first()
        filex_available = Filex.query.filter_by(area=checkUser.area).with_entities(Filex.id).all()
        ids_disponibles = [result[0] for result in filex_available]
        if checkUser.area != 'AGCCTYL':
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                # stations_available = Station.query.all()
                stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).filter_by(status2='Available').all()
                # stations_available = Station.query.filter_by(status2='Available').all()
        else:
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                stations_available = Station.query.all()
                # stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                # stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).filter_by(status2='Available').all()
                stations_available = Station.query.filter_by(status2='Available').all()
        return stations_schema.dump(stations_available)
        

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