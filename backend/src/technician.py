from flask import Blueprint
from flask import request
from flask import url_for
from src.db import db, Technician, ma, User
from sqlalchemy import exc
from flask_jwt_extended import jwt_required, get_jwt_identity


bp = Blueprint("technician", __name__)
class TechnicianSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "nombre", "apellido", "area")

technician_schema = TechnicianSchema()
technicians_schema = TechnicianSchema( many = True )


@bp.route("/technician", methods=["POST"])
@jwt_required()
def technician():
    try:
        nombre = request.json.get('nombre')
        apellido = request.json.get('apellido')
        area = request.json.get('area')
        technician = Technician(nombre = nombre, apellido = apellido, area = area)
        r = db.session.add(technician)
        db.session.commit()
        response = {"id": technician.id }
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400


@bp.route('/technician/<id>', methods = ['GET'])
@jwt_required()
def get_technician(id): 
    try:
        technician = Technician.query.get(id)
        return technician_schema.dump(technician)
    except:
        response = {"message": "input error"}
        return response, 400
    

@bp.route("/technician/", methods = ['GET'])
@jwt_required()
def get_all_technicians():
    try:
        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        if checkUser.area != 'AGCCTYL':
            all_technicians = Technician.query.filter_by(area = checkUser.area).all()
        else:
            all_technicians = Technician.query.all()

        return technicians_schema.dump(all_technicians)
    except:
        response = {"message": "server error"}
        return response, 500


@bp.route("/technician/<id>/delete_technician", methods = ['DELETE'])
@jwt_required()
def delete_technician(id):
    try:
        technician=Technician.query.get(id)
        db.session.delete(technician)
        db.session.commit()
        return technician_schema.jsonify(technician)
    except:
        response = {"message": "server error"}
        return response, 500



