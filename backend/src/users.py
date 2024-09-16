from flask import Blueprint
from flask import request, jsonify
from flask_cors import cross_origin
from src.db import User, ma, db
from sqlalchemy import exc
from werkzeug.security import check_password_hash, generate_password_hash
import base64

from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from flask_jwt_extended import jwt_required, unset_jwt_cookies, get_jwt, get_jwt_identity


bp = Blueprint("user", __name__)


checkUser = None

# @jwt_required()
# def verify_password(usuario, password):
#     global checkUser
#     try:               
#         checkUser = User.query.filter_by(usuario=usuario).first()
#         if checkUser is not None:
#             hashed_password = checkUser.password
#             return check_password_hash(hashed_password, password)
#         else:
#             return False
#     except exc.SQLAlchemyError:
#         response = { "message": "database error" }
#         return response, 500
#     except Exception as e:
#         response = { "message": "input error" }
#         return response, 400


@bp.route("/change_password", methods=["PATCH"])
@jwt_required()
def change_password():
    try:

        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        new_password = request.json.get('new_pass')
        confirm_new_password = request.json.get('new_pass_confirm')

        if new_password == confirm_new_password:
            checkUser.password = generate_password_hash(new_password)
            db.session.commit()
            
            response = { "message": "Password cambiado correctamente" }
            return response, 200
        else:
            return "Error al cambiar el password", 401
        
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
        checkUser = User.query.filter_by(usuario=usuario).first()

        if checkUser and check_password_hash(checkUser.password, password):
            additional_claims = { "area": checkUser.area, "perfil": checkUser.perfil, "usuario": checkUser.usuario }
            access_token = create_access_token(identity = checkUser.id, additional_claims = additional_claims)
            refresh_token = create_refresh_token(identity = checkUser.id)
            response = jsonify({"message": "Login successful"})
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)

            return response, 201
        else:
            return jsonify(message = "Unauthorized"), 401
    except:
        return 401
    

@bp.route("/logout", methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response, 200

@bp.route("/check_user", methods=["GET"])
@jwt_required()
def login_status():
    try:
        user_id = get_jwt_identity() 
        if user_id:
            jwt_data = get_jwt()
            area = jwt_data["area"]
            perfil = jwt_data["perfil"]
            usuario = jwt_data["usuario"]
            return jsonify(loggedIn=True, user_id = user_id, area= area, perfil = perfil, usuario = usuario), 200
                
        else:
            return jsonify({"loggedIn": False}), 401
    except Exception as e:
        return jsonify({"loggedIn": False, "error": str(e)}), 401



