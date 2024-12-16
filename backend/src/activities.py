from flask import Blueprint
from flask import request
from src.db import db, CaseFile, Station, TechMeasurement, technician_tech_measurement, technician_station, Technician, file_tracking, ma, User, Activity
from sqlalchemy import exc, insert, delete
from src.technician import technicians_schema
from src.station import station_schema, stations_schema
from src.tech_measurement import tech_measurements_schema, tech_measurement_schema
from flask_jwt_extended import jwt_required, get_jwt_identity


bp = Blueprint("activities", __name__)
class ActivitySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "fecha", "file_id", "detalle", "usuario")

activity_schema = ActivitySchema()
activities_schema = ActivitySchema( many = True )

@bp.route("/file/<file_id>/activity", methods=["POST"])
@jwt_required()
def new_activity(file_id):
    try:     
        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        # import pdb; pdb.set_trace()

        fecha = request.json.get('fecha')
        file_id = file_id
        detalle = request.json.get('detalle')
        usuario = checkUser.usuario
        activity = Activity(fecha = fecha, file_id = file_id, detalle = detalle, usuario = usuario)
        db.session.add(activity)
        db.session.commit()
        response = {"activity_id": activity.id }
        return response, 201
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except Exception as e:
        response = { "message": "input error" }
        return response, 400


@bp.route("/file/<file_id>/activities", methods = ['GET'])
@jwt_required()
def get_files_activities(file_id):

    try:

        activities = Activity.query.filter_by(file_id = file_id)
        return activities_schema.dump(activities)
        
    except:
        response = {"message": "server error"}
        return response, 500

