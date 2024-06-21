from flask import Blueprint
from flask import request
from flask import url_for
from src.db import db, NonIonizingRadiation, ma, User
from sqlalchemy import exc
from src.users import auth

bp = Blueprint("non_ionizing_radiation", __name__)
class NonIonizingRadiationSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "expediente", "fecha", "hora", "area", "cantidad", "valor_maximo", "provincia", "localidad", "tipo", "observaciones", "id_technician1", "id_technician2")

non_ionizing_radiation_schema = NonIonizingRadiationSchema()
non_ionizing_radiations_schema = NonIonizingRadiationSchema( many = True )


@bp.route("/non_ionizing_radiation/create", methods=["POST"])
@auth.login_required
def non_ionizing_radiation():
    # import pdb; pdb.set_trace()

    try:
        expediente = request.json.get('expediente')
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        area = request.json.get('area')
        cantidad = request.json.get('cantidad')
        valor_maximo = request.json.get('valor_maximo')
        provincia = request.json.get('provincia')
        localidad = request.json.get('localidad')
        observaciones = request.json.get('observaciones')
        tipo = request.json.get('tipo')
        id_technician1 = request.json.get('id_technician1')
        id_technician2 = request.json.get('id_technician2')
        non_ionizing_radiation = NonIonizingRadiation( expediente = expediente, fecha = fecha, hora = hora, area = area, cantidad = cantidad, valor_maximo = valor_maximo, provincia = provincia, localidad = localidad, tipo = tipo, observaciones = observaciones, id_technician1 = id_technician1, id_technician2 = id_technician2)
        r = db.session.add(non_ionizing_radiation)
        db.session.commit()
        response = {"id": non_ionizing_radiation.id }
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400


@bp.route('/non_ionizing_radiation/<id>', methods = ['GET'])
@auth.login_required
def get_non_ionizing_radiations(id): 
    try:
        non_ionizing_radiation = NonIonizingRadiation.query.get(id)
        return non_ionizing_radiation_schema.dump(non_ionizing_radiation)
    except:
        response = {"message": "input error"}
        return response, 400
    

@bp.route("/non_ionizing_radiation/", methods = ['GET'])
@auth.login_required
def get_all_non_ionizing_radiations():
    try:
        # import pdb; pdb.set_trace()
        usuario = auth.current_user()
        checkUser= User.query.filter_by(usuario=usuario).first()
        if checkUser.area != 'AGCCTYL':
            all_non_ionizing_radiations = NonIonizingRadiation.query.filter_by(area = checkUser.area).all()
        else:
            all_non_ionizing_radiations = NonIonizingRadiation.query.all()

        return non_ionizing_radiations_schema.dump(all_non_ionizing_radiations)
    except:
        response = {"message": "server error"}
        return response, 500


@bp.route("/non_ionizing_radiation/<id>/delete_non_ionizing_radiation", methods = ['DELETE'])
@auth.login_required
def delete_technician(id):
    try:
        non_ionizing_radiation=NonIonizingRadiation.query.get(id)
        db.session.delete(non_ionizing_radiation)
        db.session.commit()
        return non_ionizing_radiation_schema.jsonify(non_ionizing_radiation)
    except:
        response = {"message": "server error"}
        return response, 500



