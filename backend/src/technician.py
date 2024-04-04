from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from src.db import db, Technician, ma, User
from sqlalchemy import exc
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from src.users import verify_password, auth, checkUser

bp = Blueprint("technician", __name__)
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



class TechnicianSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "nombre", "apellido", "area")

technician_schema = TechnicianSchema()
technicians_schema = TechnicianSchema( many = True )


@bp.route("/technician", methods=["POST"])
@auth.login_required
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
@auth.login_required
def get_technician(id): 
    try:
        # import pdb; pdb.set_trace()
        technician = Technician.query.get(id)
        return technician_schema.dump(technician)
    except:
        response = {"message": "input error"}
        return response, 400
    

@bp.route("/technician/", methods = ['GET'])
@auth.login_required
def get_all_technicians():
    try:
        # all_technicians = Technician.query.all()
        usuario = auth.current_user()
        checkUser= User.query.filter_by(usuario=usuario).first()
        if checkUser.area != 'AGCCTYL':
            all_technicians = Technician.query.filter_by(area = checkUser.area).all()
        else:
            all_technicians = Technician.query.all()

        # import pdb; pdb.set_trace()
        return technicians_schema.dump(all_technicians)
    except:
        response = {"message": "server error"}
        return response, 500


@bp.route("/technician/<id>/delete_technician", methods = ['DELETE'])
@auth.login_required
def delete_technician(id):
    try:
        technician=Technician.query.get(id)
        db.session.delete(technician)
        db.session.commit()
        return technician_schema.jsonify(technician)
    except:
        response = {"message": "server error"}
        return response, 500



