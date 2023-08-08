from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from src.db import db, TechMeasurement, ma
from sqlalchemy import exc




bp = Blueprint("tech_measurement", __name__)


class TechMeasurementSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "id_file", "fecha", "hora", "area", "id_location", "distancia", "azimut", "mic", "claseEmision", "anchoBanda", "unidad", "noEsencial1", "micNoEsencial1", "noEsencial2", "micNoEsencial2", "noEsencial3", "micNoEsencial3", "resultadoComprob", "id_technician")

tech_measurement_schema = TechMeasurementSchema()
tech_measurements_schema = TechMeasurementSchema( many = True )

@bp.route('/tech_measurement/<id>', methods = ['GET'])
def get_tech_measurement(id):
    try:
        import pdb; pdb.set_trace()
        tech_measurement = TechMeasurement.query.get(id)
        return tech_measurement_schema.dump(tech_measurement)
    except:
        response = {"message": "input error"}
        return response, 400
    
@bp.route("/tech_measurement/", methods = ['GET'])
def get_all_tech_measurements():
    try:
        all_tech_measurements = TechMeasurement.query.all()
        # import pdb; pdb.set_trace()
        return tech_measurements_schema.dump(all_tech_measurements)
    except:
        response = {"message": "server error"}
        return response, 500


@bp.route("/tech_measurement", methods=["POST"])
def technician():
    try:
        # nombre = request.json.get('nombre')
        # apellido = request.json.get('apellido')
        import pdb; pdb.set_trace()

        id_file = request.json.get('id_file')
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        area = request.json.get('area')
        id_location = request.json.get('id_location')
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
        id_technician = request.json.get('id_technician')

        tech_measurement = TechMeasurement(id_file = id_file, fecha = fecha, hora = hora, area = area, id_location = id_location, distancia = distancia, azimut = azimut, mic = mic, claseEmision = claseEmision, anchoBanda = anchoBanda, unidad = unidad, noEsencial1 = noEsencial1, micNoEsencial1 = micNoEsencial1, noEsencial2 = noEsencial2, micNoEsencial2 = micNoEsencial2, noEsencial3 = noEsencial3, micNoEsencial3 = micNoEsencial3, resultadoComprob = resultadoComprob, id_technician = id_technician)
        r = db.session.add(tech_measurement)
        db.session.commit()
        response = {"id": tech_measurement.id }
        # import pdb; pdb.set_trace()
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400

    



