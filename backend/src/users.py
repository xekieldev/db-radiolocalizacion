from flask import Blueprint
from flask import request
from src.db import User, ma, db
from sqlalchemy import exc
from werkzeug.security import check_password_hash, generate_password_hash
import base64
from flask_httpauth import HTTPBasicAuth


bp = Blueprint("user", __name__)
auth = HTTPBasicAuth()

checkUser = None

@auth.verify_password
def verify_password(usuario, password):
    global checkUser
    try:               
        checkUser = User.query.filter_by(usuario=usuario).first()
        if checkUser is not None:
            hashed_password = checkUser.password
            return check_password_hash(hashed_password, password)
        else:
            return False
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except Exception as e:
        response = { "message": "input error" }
        return response, 400


# @auth.verify_password
@bp.route("/change_password", methods=["PATCH"])
def change_password():
    try:
        usuario = request.json.get('user')
        password = request.json.get('pass')
        new_password = request.json.get('new_pass')
        confirm_new_password = request.json.get('new_pass_confirm')

        if verify_password(usuario, password):
            if new_password == confirm_new_password:
                checkUser.password = generate_password_hash(new_password)
                db.session.commit()
                
                response = { "message": "Password cambiado correctamente" }
                return response, 200
            else:
                return "Error al cambiar el password", 401
        else:
            return "Error de login", 401
        
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except Exception as e:
        response = { "message": "input error" }
        return response, 400

@bp.route("/login", methods=["POST"])
def user():
    try:
        usuario = request.json.get('user')
        password = request.json.get('pass')
        if verify_password(usuario, password):
            cadena_codificada = base64.b64encode((usuario + ':' + password).encode()).decode()
            return cadena_codificada, 200
        else:
            return "Error de login", 401
    except:
        return 401



