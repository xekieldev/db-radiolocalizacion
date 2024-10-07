from flask import Blueprint
from flask import request
from werkzeug.exceptions import abort
from src.db import Station, Technician, TechMeasurement, ma, User, db, technician_station, technician_tech_measurement
from src.technician import technicians_schema
from src.tech_measurement import tech_measurement_schema, tech_measurements_schema
from sqlalchemy import exc, insert, delete
from flask_jwt_extended import jwt_required, get_jwt_identity



bp = Blueprint("station", __name__)

class StationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id","file_id", "expediente", "fecha", "hora", "area", "status", "identificacion", "emplazamiento", "servicio", "frecuencia", "unidad", "claseEmision",
                   "irradiante", "polarizacion", "cantidad", "altura", "tipoVinculo", "frecuenciaVinc",
                     "unidadVinc", "irradianteVinc", "polarizacionVinc", "provincia", "localidad",
                       "domicilio", "latitud", "longitud", "observaciones", "related_station_id")

station_schema = StationSchema()
stations_schema = StationSchema(many=True)

@bp.route("/file/<id>/station", methods=["POST"])
@jwt_required()
def station(id):
    try:
        file_id = id
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        area = request.json.get('area')
        id_technician1 = request.json.get('id_technician1')
        id_technician2 = request.json.get('id_technician2')
        identificacion = request.json.get('identificacion')
        emplazamiento = request.json.get('emplazamiento')
        servicio = request.json.get('servicio')
        frecuencia = request.json.get('frecuencia')
        unidad = request.json.get('unidad')
        claseEmision = request.json.get('claseEmision')
        irradiante = request.json.get('irradiante')
        polarizacion = request.json.get('polarizacion')
        cantidad = request.json.get('cantidad')
        altura = request.json.get('altura')
        tipoVinculo = request.json.get('tipoVinculo')
        frecuenciaVinc = request.json.get('frecuenciaVinc')
        unidadVinc = request.json.get('unidadVinc')
        irradianteVinc = request.json.get('irradianteVinc')
        polarizacionVinc = request.json.get('polarizacionVinc')
        provincia = request.json.get('provincia')
        localidad = request.json.get('localidad')
        domicilio = request.json.get('domicilio')
        latitud = request.json.get('latitud')
        longitud = request.json.get('longitud')
        observaciones = request.json.get('observaciones')
        related_station_id = request.json.get('related_station_id')
                
        station = Station(file_id = file_id, fecha = fecha, hora = hora, area = area, id_technician1 = id_technician1, id_technician2 = id_technician2, identificacion = identificacion, emplazamiento = emplazamiento, servicio = servicio, frecuencia = frecuencia, unidad = unidad, claseEmision = claseEmision, irradiante = irradiante, polarizacion = polarizacion, cantidad = cantidad, altura = altura, tipoVinculo = tipoVinculo, frecuenciaVinc = frecuenciaVinc, unidadVinc = unidadVinc, irradianteVinc = irradianteVinc, polarizacionVinc = polarizacionVinc, provincia = provincia, localidad = localidad, domicilio = domicilio, latitud = latitud, longitud = longitud, observaciones = observaciones, related_station_id = related_station_id)
        db.session.add(station)

        db.session.commit()
        
        stmt1 = (
        insert(technician_station).
        values(id_station = station.id, id_technician = request.json.get('id_technician1'))
        )
        stmt2 = (
        insert(technician_station).
        values(id_station = station.id, id_technician = request.json.get('id_technician2'))
        )
        session = db.session
        session.execute(stmt1)
        session.execute(stmt2)
        session.commit()
        
        response = {"id_station": station.id }
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400

    
@bp.route('/station/<id>', methods = ['GET'])
@jwt_required()
def get_station(id):
    try:
        station = Station.query.get(id)
        technicians = (db.session.query(Technician).join(technician_station).filter(technician_station.c.id_station==id))
        combined_return = {"station": station_schema.dump(station),
                           "technicians": technicians_schema.dump(technicians)}
        return combined_return
    except Exception as e:
        print(e)
        response = {"message": "input error"}
        return response, 400

    
@bp.route("/station", methods = ['GET'])
@jwt_required()
def get_all_stations():

    try:
        include_deleted = request.args.get('includeDeleted')
        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        station_available = Station.query.filter_by(area=checkUser.area).with_entities(Station.id).all()
        ids_disponibles = [result[0] for result in station_available]
        if checkUser.area != 'AGCCTYL':
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).filter_by(status='Available').all()
        else:
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                stations_available = Station.query.all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                stations_available = Station.query.filter_by(status='Available').all()
        return stations_schema.dump(stations_available)
        

    except:
        response = {"message": "server error"}
        return response, 500

@bp.route('/file/<file_id>/station/<id>/edit', methods = ['PUT'])
@jwt_required()
def edit_station(file_id, id):
    try:
        station = Station.query.get(id)
        technicians = (db.session.query(Technician).join(technician_station).filter(technician_station.c.id_station==id))
        
        if station:
            file_id = file_id
            fecha = request.json.get('fecha')
            hora = request.json.get('hora')
            area = request.json.get('area')
            id_technician1 = request.json.get('id_technician1')
            id_technician2 = request.json.get('id_technician2')
            identificacion = request.json.get('identificacion')
            emplazamiento = request.json.get('emplazamiento')
            servicio = request.json.get('servicio')
            frecuencia = request.json.get('frecuencia')
            unidad = request.json.get('unidad')
            claseEmision = request.json.get('claseEmision')
            irradiante = request.json.get('irradiante')
            polarizacion = request.json.get('polarizacion')
            cantidad = request.json.get('cantidad')
            altura = request.json.get('altura')
            tipoVinculo = request.json.get('tipoVinculo')
            frecuenciaVinc = request.json.get('frecuenciaVinc')
            unidadVinc = request.json.get('unidadVinc')
            irradianteVinc = request.json.get('irradianteVinc')
            polarizacionVinc = request.json.get('polarizacionVinc')
            provincia = request.json.get('provincia')
            localidad = request.json.get('localidad')
            domicilio = request.json.get('domicilio')
            latitud = request.json.get('latitud')
            longitud = request.json.get('longitud')
            observaciones = request.json.get('observaciones')

            station.file_id = file_id
            station.fecha = fecha
            station.hora = hora
            station.area = area
            station.id_technician1 = id_technician1
            station.id_technician2 = id_technician2
            station.identificacion = identificacion
            station.emplazamiento = emplazamiento
            station.servicio = servicio
            station.frecuencia = frecuencia
            station.unidad = unidad
            station.claseEmision = claseEmision
            station.irradiante = irradiante
            station.polarizacion = polarizacion
            station.cantidad = cantidad
            station.altura = altura
            station.tipoVinculo = tipoVinculo
            station.frecuenciaVinc = frecuenciaVinc
            station.unidadVinc = unidadVinc
            station.irradianteVinc = irradianteVinc
            station.polarizacionVinc = polarizacionVinc
            station.provincia = provincia
            station.localidad = localidad
            station.domicilio = domicilio
            station.latitud = latitud
            station.longitud = longitud
            station.observaciones = observaciones

            db.session.commit()
        else:
            return {"error": "id not found"}, 404
        

        stmt0 = (
        delete(technician_station).
        where(technician_station.c.id_station == station.id)
        )
        session = db.session
        session.execute(stmt0)

        stmt1 = (
        insert(technician_station).
        values(id_station = station.id, id_technician = request.json.get('id_technician1'))
        )
        stmt2 = (
        insert(technician_station).
        values(id_station = station.id, id_technician = request.json.get('id_technician2'))
        )

        session = db.session
        session.execute(stmt1)
        session.execute(stmt2)
        db.session.commit()


        response = {'file_id': station.file_id, 'station_id': station.id}
        return response

    except Exception as e:
        print(f"Error: {e}")
        response = {"message": "input error"}
        return response, 400


@bp.route('/file/<file_id>/station/<id>', methods = ['DELETE'])
@jwt_required()
def delete_station(file_id, id):
    try:
        station = Station.query.get(id)
        station.status = 'Deleted'
        db.session.commit()
        response = {'file_id': station.file_id, 'station_id': station.id}
        return response

    except:
        response = {"message": "input error"}
        return response, 400
    
@bp.route("/file/<file_id>/station/<id>/create_tech_measurement", methods=["POST"])
@jwt_required()
def tech_measurement(file_id, id):
    # import pdb; pdb.set_trace()
    try:
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        puntoMedicion = request.json.get('puntoMedicion')
        # import pdb; pdb.set_trace()

        station_id = id
        frecMedida = request.json.get('frecMedida')
        unidadFrecMedida = request.json.get('unidadFrecMedida')
        anchoBanda =  request.json.get('anchoBanda')
        unidadBW = request.json.get('unidadBW')
        domicilio = request.json.get('domicilio')
        localidad = request.json.get('localidad')
        provincia = request.json.get('provincia')
        latitud = request.json.get('latitud')
        longitud = request.json.get('longitud')
        distancia = request.json.get('distancia')
        azimut = request.json.get('azimut')
        observaciones = request.json.get('observaciones')
        domicilioTestigo = request.json.get('domicilioTestigo')
        localidadTestigo = request.json.get('localidadTestigo')
        provinciaTestigo = request.json.get('provinciaTestigo')
        latitudTestigo = request.json.get('latitudTestigo')
        longitudTestigo = request.json.get('longitudTestigo')
        distanciaTestigo = request.json.get('distanciaTestigo')
        azimutTestigo = request.json.get('azimutTestigo')
        eMedido = request.json.get('eMedido')
        eTestigo = request.json.get('eTestigo')
        eCorregido = request.json.get('eCorregido')
        incertidumbre = request.json.get('incertidumbre')
        equipamiento = request.json.get('equipamiento')
        resultadoComprob = request.json.get('resultadoComprob')
        id_technician1 = request.json.get('id_technician1')
        id_technician2 = request.json.get('id_technician2')


        tech_measurement = TechMeasurement(fecha = fecha, hora = hora, puntoMedicion = puntoMedicion, station_id = station_id, frecMedida = frecMedida, unidadFrecMedida = unidadFrecMedida, anchoBanda = anchoBanda, unidadBW = unidadBW, domicilio = domicilio, localidad = localidad, provincia = provincia, latitud = latitud, longitud = longitud, distancia = distancia, azimut = azimut, observaciones = observaciones, domicilioTestigo = domicilioTestigo, localidadTestigo = localidadTestigo, provinciaTestigo = provinciaTestigo, latitudTestigo = latitudTestigo, longitudTestigo = longitudTestigo, distanciaTestigo = distanciaTestigo, azimutTestigo = azimutTestigo, eMedido = eMedido, eTestigo = eTestigo, eCorregido = eCorregido, incertidumbre = incertidumbre, equipamiento = equipamiento, resultadoComprob = resultadoComprob, id_technician1 = id_technician1, id_technician2 = id_technician2)
        
        r = db.session.add(tech_measurement)
        db.session.commit()
        stmt1 = (
        insert(technician_tech_measurement).
        values(id_tech_measurement = tech_measurement.id, id_technician = request.json.get('id_technician1'))
        )
        stmt2 = (
        insert(technician_tech_measurement).
        values(id_tech_measurement = tech_measurement.id, id_technician = request.json.get('id_technician2'))
        )
        session = db.session
        session.execute(stmt1)
        session.execute(stmt2)
        session.commit()
       
        response = {"id": tech_measurement.id }

        return response, 201 
    except exc.SQLAlchemyError as e:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400
    

@bp.route('/file/<file_id>/station/<id>/tech_measurement', methods = ['GET'])
@jwt_required()
def get_tech_measurement(file_id, id):
    try:
        include_deleted = request.args.get('includeDeleted')
        # import pdb; pdb.set_trace()
        if include_deleted and include_deleted.lower() == 'true':
            # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
            tech_measurement = TechMeasurement.query.filter_by(station_id=id).all()

        else:
            # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
            station_available = Station.query.filter_by(status='Available').all() 
            tech_measurement = TechMeasurement.query.filter_by(station_id=id, status='Available').all()
        
        # Rehacer query: https://stackoverflow.com/questions/8603088/sqlalchemy-in-clause
        technicians = db.session.query(Technician).join(technician_tech_measurement).join(TechMeasurement).filter(TechMeasurement.station_id == id).all()

        combined_return = {
                            "techMeasurement": tech_measurements_schema.dump(tech_measurement),
                            "technicians":  technicians_schema.dump(technicians)

        }
        return combined_return
    except Exception as e:
        print(e)

        response = {"message": "input error"}
        return response, 400
    

@bp.route("/file/<file_id>/station/<id_station>/delete_tech_measurement/<id_tech_measurement>", methods = ['DELETE'])
@jwt_required()
def delete_tech_measurement(file_id, id_station, id_tech_measurement):
    try:
        tech_measurement = TechMeasurement.query.filter_by(station_id=id_station, id=id_tech_measurement).first()
        tech_measurement.status='Deleted'
        db.session.commit()
        return tech_measurement_schema.dump(tech_measurement)
    except:
        response = {"message": "server error"}
        return response, 500


@bp.route('/file/<file_id>/station/<id>', methods = ['PUT'])
@jwt_required()
def update_related_station(file_id, id):
    try:
       
        related_station_id = request.json.get('related_station_id')
        station = Station.query.get(id)
        station.related_station_id = related_station_id
        db.session.commit()
        response = { "file_id": station.file_id,
                     'station_id': station.id
                    }
        return response

    except:
        response = {"message": "input error"}
        return response, 400
    
@bp.route("/file/<file_id>/stations", methods = ['GET'])
@jwt_required()
def get_stations_per_file(file_id):

    try:
        include_deleted = request.args.get('includeDeleted')
        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        station_available = Station.query.filter_by(file_id=file_id).with_entities(Station.id).all()
        ids_disponibles = [result[0] for result in station_available]
        # import pdb; pdb.set_trace()
        # if checkUser.area != 'AGCCTYL':
        if include_deleted and include_deleted.lower() == 'true':
            # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
            stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).all()
        else:
            # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                stations_available = Station.query.filter(Station.id.in_(ids_disponibles)).filter_by(status='Available').all()
    
        return stations_schema.dump(stations_available)
        

    except:
        response = {"message": "server error"}
        return response, 500