from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from src.db import db, Filex, Station, TechMeasurement, technician_tech_measurement, technician_file, Technician, ma
from sqlalchemy import exc, insert
from src.technician import technicians_schema
from src.station import station_schema
from src.tech_measurement import tech_measurements_schema


bp = Blueprint("filex", __name__)
class FilexSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "expediente", "fecha", "hora", "area")

filex_schema = FilexSchema()
filexs_schema = FilexSchema( many = True )

@bp.route("/file/", methods = ['GET'])
def get_all_files():
    try:
        all_files = Filex.query.all()
        # import pdb; pdb.set_trace()
        return filexs_schema.dump(all_files)
    except:
        response = {"message": "server error"}
        return response, 500

# From here I modify the code to adapt it to the new API design

@bp.route("/file", methods=["POST"])
def filex():
    # import pdb; pdb.set_trace()
    
    try:
        expediente = request.json.get('expediente')
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        area = request.json.get('area')
        status = request.json.get('status')
        id_technician1 = request.json.get('id_technician1')
        id_technician2 = request.json.get('id_technician2')
        
        filex = Filex(expediente = expediente, fecha = fecha, hora = hora, area = area, status = status, id_technician1 = id_technician1, id_technician2 = id_technician2)#, id_technician2 = id_technician2 ) #, technicians = technicians)
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
        # import pdb; pdb.set_trace()
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400

    
@bp.route('/file/<id>', methods = ['GET'])
def get_file(id):
    try:
        filex = Filex.query.get(id)
        station = Station.query.get(id)
        technicians = (db.session.query(Technician).join(technician_file).filter(technician_file.c.id_file==id))
        # technicians_ids = query.all()
        # combined_return = [ filex_schema.dump(filex), station_schema.dump(station), technicians_schema.dump(technicians) ]
        combined_return = {"file": filex_schema.dump(filex),
                           "station": station_schema.dump(station),
                           "technicians": technicians_schema.dump(technicians)}
        return combined_return
    except Exception as e:
        # import pdb; pdb.set_trace()
        print(e)
        response = {"message": "input error"}
        return response, 400



@bp.route('/file', methods = ['GET'])
def get_available_files():
    try:
        include_deleted = request.args.get('includeDeleted')

        if include_deleted and include_deleted.lower() == 'true':
            # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
            filex_available = Filex.query.all()
        else:
            # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
            filex_available = Filex.query.filter_by(status='Available').all()
        # import pdb; pdb.set_trace()

        return filexs_schema.dump(filex_available)

    except:
        response = {"message": "input error"}
        return response, 400
    
@bp.route('/file/<id>', methods = ['PUT'])
def delete_file(id):
    try:
        filex = Filex.query.get(id)
        filex.status = 'Deleted'
        # import pdb; pdb.set_trace()
        db.session.commit()
        response = {'id_file': filex.id}
        return response

    except:
        response = {"message": "input error"}
        return response, 400


@bp.route("/file/<id>/tech_measurement", methods=["POST"])
def tech_measurement(id):
    try:
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        area = request.json.get('area')
        file_id = id
        distancia = request.json.get('distancia')
        azimut = request.json.get('azimut')
        mic = request.json.get('mic')
        claseEmision = request.json.get('claseEmision')
        anchoBanda =  request.json.get('anchoBanda')
        unidad = request.json.get('unidad')
        noEsencial1 = request.json.get('noEsencial1')
        micNoEsencial1 = request.json.get('micNoEsencial1')
        noEsencial2 = request.json.get('noEsencial2')
        micNoEsencial2 = request.json.get('micNoEsencial2')
        noEsencial3 = request.json.get('noEsencial2')
        micNoEsencial3 = request.json.get('micNoEsencial3')
        resultadoComprob = request.json.get('resultadoComprob')
        id_technician1 = request.json.get('id_technician1')
        id_technician2 = request.json.get('id_technician2')


        tech_measurement = TechMeasurement(fecha = fecha, hora = hora, area = area, file_id = file_id, distancia = distancia, azimut = azimut, mic = mic, claseEmision = claseEmision, anchoBanda = anchoBanda, unidad = unidad, noEsencial1 = noEsencial1, micNoEsencial1 = micNoEsencial1, noEsencial2 = noEsencial2, micNoEsencial2 = micNoEsencial2, noEsencial3 = noEsencial3, micNoEsencial3 = micNoEsencial3, resultadoComprob = resultadoComprob, id_technician1 = id_technician1, id_technician2 = id_technician2)
       
        r = db.session.add(tech_measurement)
        db.session.commit()
        # import pdb; pdb.set_trace()
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
        # print(f"Error de SQLAlchemy: {e}")
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400
    

@bp.route('/file/<id>/tech_measurement', methods = ['GET'])
def get_tech_measurement(id):
    try:
        tech_measurement = TechMeasurement.query.filter_by(file_id=id).all()
        technicians = (db.session.query(Technician).join(technician_tech_measurement).filter(technician_tech_measurement.c.id_tech_measurement==id))

        # import pdb; pdb.set_trace()
        combined_return = {
                            "Tech Measurements": tech_measurements_schema.dump(tech_measurement),
                            "Technicians":  technicians_schema.dump(technicians)

        }
        return combined_return
    except Exception as e:
        print(e)
        import pdb; pdb.set_trace()

        response = {"message": "input error"}
        return response, 400
