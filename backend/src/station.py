from flask import Blueprint
from flask import request
from werkzeug.exceptions import abort
from src.db import Station, ma, User, Filex
from src.users import auth


bp = Blueprint("station", __name__)

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
                stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).filter_by(status2='Available').all()
        else:
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                stations_available = Station.query.all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                stations_available = Station.query.filter_by(status2='Available').all()
        return stations_schema.dump(stations_available)
        

    except:
        response = {"message": "server error"}
        return response, 500

