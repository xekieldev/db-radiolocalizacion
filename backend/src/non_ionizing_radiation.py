from flask import Blueprint
from flask import request
from flask import url_for
from src.db import db, NonIonizingRadiation, ma, User, CaseFile, technician_nir, Technician
from src.technician import technicians_schema
from sqlalchemy import exc, insert
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify


bp = Blueprint("non_ionizing_radiation", __name__)
class NonIonizingRadiationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "file_id", "fecha", "hora", "area_asignada", "cantidad", "valor_maximo", "tipo", "observaciones", "id_technician1", "id_technician2")

non_ionizing_radiation_schema = NonIonizingRadiationSchema()
non_ionizing_radiations_schema = NonIonizingRadiationSchema( many = True )


@bp.route('/file/<id>/non_ionizing_radiation', methods=["POST"])
@jwt_required()
def non_ionizing_radiation(id):
    try:
        file_id = id
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        cantidad = request.json.get('cantidad')
        valor_maximo = request.json.get('valor_maximo')
        observaciones = request.json.get('observaciones')
        id_technician1 = request.json.get('id_technician1')
        id_technician2 = request.json.get('id_technician2')
        non_ionizing_radiation = NonIonizingRadiation(file_id = file_id, fecha = fecha, hora = hora, cantidad = cantidad, valor_maximo = valor_maximo, observaciones = observaciones, id_technician1 = id_technician1, id_technician2 = id_technician2)

        r = db.session.add(non_ionizing_radiation)
        db.session.commit()
        stmt1 = (
        insert(technician_nir).
        values(id_nir = non_ionizing_radiation.id, id_technician = request.json.get('id_technician1'))
        )
        stmt2 = (
        insert(technician_nir).
        values(id_nir = non_ionizing_radiation.id, id_technician = request.json.get('id_technician2'))
        )
        session = db.session
        session.execute(stmt1)
        session.execute(stmt2)
        session.commit()

        response = {"id_nir": non_ionizing_radiation.id }
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400


@bp.route('/non_ionizing_radiation/<id>', methods = ['GET'])
@jwt_required()
def get_non_ionizing_radiations(id): 
    try:
        non_ionizing_radiation = NonIonizingRadiation.query.get(id)
        technicians = (db.session.query(Technician).join(technician_nir).filter(technician_nir.c.id_nir==id))
        return {"nir": non_ionizing_radiation_schema.dump(non_ionizing_radiation),
                "technicians": technicians_schema.dump(technicians)}
                
    except:
        response = {"message": "input error"}
        return response, 400
    

@bp.route("/non_ionizing_radiation/", methods = ['GET'])
@jwt_required()
def get_all_non_ionizing_radiations():
    try:
        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        if checkUser.area != 'AGCCTYL':
            all_non_ionizing_radiations = db.session.query(NonIonizingRadiation, CaseFile.fecha, CaseFile.hora, CaseFile.localidad, CaseFile.provincia, CaseFile.expediente, CaseFile.area_asignada).join(CaseFile, NonIonizingRadiation.file_id == CaseFile.id).filter_by(area_asignada = checkUser.area).all()
        else:
            all_non_ionizing_radiations = db.session.query(NonIonizingRadiation, CaseFile.fecha, CaseFile.hora, CaseFile.localidad, CaseFile.provincia, CaseFile.expediente, CaseFile.area_asignada).join(CaseFile, NonIonizingRadiation.file_id == CaseFile.id).all()
        return jsonify([{ **{col.name: getattr(row.NonIonizingRadiation, col.name) for col in NonIonizingRadiation.__table__.columns}, "fecha": row.fecha, "hora": row.hora,"expediente": row.expediente, "area_asignada": row.area_asignada, "localidad": row.localidad, "provincia": row.provincia } for row in all_non_ionizing_radiations])
    except:
        response = {"message": "server error"}
        return response, 500


@bp.route("/file/<file_id>/non_ionizing_radiation/", methods = ['DELETE'])
@jwt_required()
def delete_nir(file_id):
    try:
        non_ionizing_radiation=NonIonizingRadiation.query.filter_by(file_id = file_id).first()
        db.session.delete(non_ionizing_radiation)
        db.session.commit()
        return non_ionizing_radiation_schema.jsonify(non_ionizing_radiation)
    except:
        response = {"message": "server error"}
        return response, 500



# @bp.route("/file/<file_id>/non_ionizing_radiation/", methods = ['GET'])
# @jwt_required()
# def get_nir_measurements_in_file(file_id):
#     # import pdb; pdb.set_trace()

#     try:

#         # import pdb; pdb.set_trace()
#         usuario_id = get_jwt_identity()      
#         checkUser= User.query.filter_by(id = usuario_id).first()
#         if checkUser.area != 'AGCCTYL':
#             all_non_ionizing_radiations = NonIonizingRadiation.query.filter_by(area_asignada = checkUser.area, file_id = file_id).all()
#         else:
#             all_non_ionizing_radiations = NonIonizingRadiation.query.all()

#         return non_ionizing_radiations_schema.dump(all_non_ionizing_radiations)
#     except:
#         response = {"message": "server error"}
#         return response, 500

@bp.route("/file/<file_id>/non_ionizing_radiation/", methods=['GET'])
@jwt_required()
def get_nir_measurements_in_file(file_id):
    try:
        usuario_id = get_jwt_identity()      
        checkUser = User.query.filter_by(id=usuario_id).first()

        if checkUser.area != 'AGCCTYL':
            all_non_ionizing_radiations = NonIonizingRadiation.query.filter(CaseFile.area_asignada == checkUser.area, NonIonizingRadiation.file_id == file_id).all()
        else:
            all_non_ionizing_radiations = NonIonizingRadiation.query.filter_by(file_id=file_id).all()

        return non_ionizing_radiations_schema.dump(all_non_ionizing_radiations)
    except:
        response = {"message": "server error"}
        return response, 500