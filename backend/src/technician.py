from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from src.db import db, Technician, ma
from sqlalchemy import exc


bp = Blueprint("technician", __name__)


class TechnicianSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "nombre", "apellido")

technician_schema = TechnicianSchema()
technicians_schema = TechnicianSchema( many = True )


@bp.route("/technician", methods=["POST"])
def technician():
    try:
        nombre = request.json.get('nombre')
        apellido = request.json.get('apellido')
        technician = Technician(nombre = nombre, apellido = apellido)
        r = db.session.add(technician)
        db.session.commit()
        response = {"id": technician.id }
        # import pdb; pdb.set_trace()
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400


@bp.route('/technician/<id>', methods = ['GET'])
def get_technician(id): 
    try:
        # import pdb; pdb.set_trace()
        technician = Technician.query.get(id)
        return technician_schema.dump(technician)
    except:
        response = {"message": "input error"}
        return response, 400
    

@bp.route("/technician/", methods = ['GET'])
def get_all_technicians():
    try:
        all_technicians = Technician.query.all()
        # import pdb; pdb.set_trace()
        return technicians_schema.dump(all_technicians)
    except:
        response = {"message": "server error"}
        return response, 500


@bp.route("/technician/<id>", methods = ['DELETE'])
def delete_technician(id):
    try:
        technician=Technician.query.get(id)
        db.session.delete(technician)
        db.session.commit()
        return technician_schema.jsonify(technician)
    except:
        response = {"message": "server error"}
        return response, 500



