from flask import Blueprint
from flask import request
from src.db import db, Filex, Station, TechMeasurement, technician_tech_measurement, technician_file, Technician, ma, User
from sqlalchemy import exc, insert, delete
from src.technician import technicians_schema
from src.station import station_schema
from src.tech_measurement import tech_measurements_schema
from src.users import auth


bp = Blueprint("filex", __name__)
class FilexSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "expediente", "fecha", "hora", "area", "status")

filex_schema = FilexSchema()
filexs_schema = FilexSchema( many = True )

@bp.route("/file/", methods = ['GET'])  
@auth.login_required
def get_all_files():
    try:
        all_files = Filex.query.all()
        return filexs_schema.dump(all_files)
    except:
        response = {"message": "server error"}
        return response, 500

# From here I modify the code to adapt it to the new API design

@bp.route("/file", methods=["POST"])
@auth.login_required
def filex():
    try:
        expediente = request.json.get('expediente')
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        area = request.json.get('area')
        id_technician1 = request.json.get('id_technician1')
        id_technician2 = request.json.get('id_technician2')
        
        filex = Filex(expediente = expediente, fecha = fecha, hora = hora, area = area, id_technician1 = id_technician1, id_technician2 = id_technician2)#, id_technician2 = id_technician2 ) #, technicians = technicians)
        db.session.add(filex)

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
                
        station = Station(identificacion = identificacion, emplazamiento = emplazamiento, servicio = servicio, frecuencia = frecuencia, unidad = unidad, claseEmision = claseEmision, irradiante = irradiante, polarizacion = polarizacion, cantidad = cantidad, altura = altura, tipoVinculo = tipoVinculo, frecuenciaVinc = frecuenciaVinc, unidadVinc = unidadVinc, irradianteVinc = irradianteVinc, polarizacionVinc = polarizacionVinc, provincia = provincia, localidad = localidad, domicilio = domicilio, latitud = latitud, longitud = longitud, observaciones = observaciones)
        db.session.add(station)

        db.session.commit()
        
        stmt1 = (
        insert(technician_file).
        values(id_file = filex.id, id_technician = request.json.get('id_technician1'))
        )
        stmt2 = (
        insert(technician_file).
        values(id_file = filex.id, id_technician = request.json.get('id_technician2'))
        )
        session = db.session
        session.execute(stmt1)
        session.execute(stmt2)
        session.commit()
        
        response = {"id_file": filex.id,
                    "id_station": station.id }
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400

    
@bp.route('/file/<id>', methods = ['GET'])
@auth.login_required
def get_file(id):
    try:
        filex = Filex.query.get(id)
        station = Station.query.get(id)
        technicians = (db.session.query(Technician).join(technician_file).filter(technician_file.c.id_file==id))
        combined_return = {"file": filex_schema.dump(filex),
                           "station": station_schema.dump(station),
                           "technicians": technicians_schema.dump(technicians)}
        return combined_return
    except Exception as e:
        print(e)
        response = {"message": "input error"}
        return response, 400



@bp.route('/file', methods = ['GET'])
@auth.login_required
def get_available_files():
    try:
        include_deleted = request.args.get('includeDeleted')
        usuario = auth.current_user()
        checkUser= User.query.filter_by(usuario=usuario).first()
        if checkUser.area != 'AGCCTYL':
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                filex_available = Filex.query.filter_by(area = checkUser.area).all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                filex_available = Filex.query.filter_by(area = checkUser.area, status='Available').all()
        else:
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                filex_available = Filex.query.all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                filex_available = Filex.query.filter_by(status='Available').all()          

        return filexs_schema.dump(filex_available)

    except:
        response = {"message": "input error"}
        return response, 400

@bp.route('/file/<id>/edit', methods = ['PUT'])
@auth.login_required
def edit_file(id):
    try:
        filex = Filex.query.get(id)
        station = Station.query.get(id)
        technicians = (db.session.query(Technician).join(technician_file).filter(technician_file.c.id_file==id))
        
        if filex:
            expediente = request.json.get('expediente')
            fecha = request.json.get('fecha')
            hora = request.json.get('hora')
            area = request.json.get('area')
            id_technician1 = request.json.get('id_technician1')
            id_technician2 = request.json.get('id_technician2')
            
            filex.expediente = expediente
            filex.fecha = fecha
            filex.hora = hora
            filex.area = area
            filex.id_technician1 = id_technician1
            filex.id_technician2 = id_technician2

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
        delete(technician_file).
        where(technician_file.c.id_file == filex.id)
        )
        session = db.session
        session.execute(stmt0)

        stmt1 = (
        insert(technician_file).
        values(id_file = filex.id, id_technician = request.json.get('id_technician1'))
        )
        stmt2 = (
        insert(technician_file).
        values(id_file = filex.id, id_technician = request.json.get('id_technician2'))
        )

        session = db.session
        session.execute(stmt1)
        session.execute(stmt2)
        db.session.commit()


        response = {'id_file': filex.id}
        return response

    except Exception as e:
        print(f"Error: {e}")
        response = {"message": "input error"}
        return response, 400

@bp.route('/file/<id>', methods = ['DELETE'])
@auth.login_required
def delete_file(id):
    try:
        filex = Filex.query.get(id)
        station = Station.query.get(id)
        filex.status = 'Deleted'
        station.status2 = 'Deleted'
        db.session.commit()
        response = {'id_file': filex.id}
        return response

    except:
        response = {"message": "input error"}
        return response, 400


@bp.route("/file/<id>/create_tech_measurement", methods=["POST"])
@auth.login_required
def tech_measurement(id):
    try:
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        puntoMedicion = request.json.get('puntoMedicion')
        file_id = id
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
        resultadoComprob = request.json.get('resultadoComprob')
        id_technician1 = request.json.get('id_technician1')
        id_technician2 = request.json.get('id_technician2')


        tech_measurement = TechMeasurement(fecha = fecha, hora = hora, puntoMedicion = puntoMedicion, file_id = file_id, frecMedida = frecMedida, unidadFrecMedida = unidadFrecMedida, anchoBanda = anchoBanda, unidadBW = unidadBW, domicilio = domicilio, localidad = localidad, provincia = provincia, latitud = latitud, longitud = longitud, distancia = distancia, azimut = azimut, observaciones = observaciones, domicilioTestigo = domicilioTestigo, localidadTestigo = localidadTestigo, provinciaTestigo = provinciaTestigo, latitudTestigo = latitudTestigo, longitudTestigo = longitudTestigo, distanciaTestigo = distanciaTestigo, azimutTestigo = azimutTestigo, eMedido = eMedido, eTestigo = eTestigo, eCorregido = eCorregido, incertidumbre = incertidumbre, resultadoComprob = resultadoComprob, id_technician1 = id_technician1, id_technician2 = id_technician2)
        
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
    

@bp.route('/file/<id>/tech_measurement', methods = ['GET'])
@auth.login_required
def get_tech_measurement(id):
    try:
        tech_measurement = TechMeasurement.query.filter_by(file_id=id).all()
        
        # Rehacer query: https://stackoverflow.com/questions/8603088/sqlalchemy-in-clause
        technicians = db.session.query(Technician).join(technician_tech_measurement).join(TechMeasurement).filter(TechMeasurement.file_id == id).all()

        combined_return = {
                            "techMeasurement": tech_measurements_schema.dump(tech_measurement),
                            "technicians":  technicians_schema.dump(technicians)

        }
        return combined_return
    except Exception as e:
        print(e)

        response = {"message": "input error"}
        return response, 400
