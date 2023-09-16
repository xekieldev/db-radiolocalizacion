from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from src.db import db, Filex, ma
from sqlalchemy import exc




bp = Blueprint("filex", __name__)


class FilexSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "expediente", "fecha", "hora", "area", "id_technician1", "id_technician2" ) #, "technicians")

filex_schema = FilexSchema()
filexs_schema = FilexSchema( many = True )

@bp.route('/file/<id>', methods = ['GET'])
def get_file(id):
    try:
        import pdb; pdb.set_trace()
        filex = Filex.query.get(id)
        return filex_schema.dump(filex)
    except:
        response = {"message": "input error"}
        return response, 400
    
@bp.route("/file/", methods = ['GET'])
def get_all_files():
    try:
        all_files = Filex.query.all()
        # import pdb; pdb.set_trace()
        return filexs_schema.dump(all_files)
    except:
        response = {"message": "server error"}
        return response, 500


@bp.route("/file", methods=["POST"])
def filex():
    # import pdb; pdb.set_trace()
    
    try:
        expediente = request.json.get('expediente')
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        area = request.json.get('area')
        # id_technician1 = request.json.get('id_technician1')
        # id_technician2 = request.json.get('id_technician2')
        # technicians = request.json.get('technicians')
        filex = Filex(expediente = expediente, fecha = fecha, hora = hora, area = area)#, id_technician1 = id_technician1, id_technician2 = id_technician2 ) #, technicians = technicians)
        r = db.session.add(filex)
        db.session.commit()
        response = {"id": filex.id }
        # import pdb; pdb.set_trace()
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400

    



