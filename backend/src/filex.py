from flask import Blueprint
from flask import request
from src.db import db, CaseFile, Station, TechMeasurement, technician_tech_measurement, technician_station, Technician, file_tracking, ma, User
from sqlalchemy import exc, insert, delete, select
from src.technician import technicians_schema
from src.station import station_schema, stations_schema
from src.tech_measurement import tech_measurements_schema, tech_measurement_schema
from src.users import auth


bp = Blueprint("case_file", __name__)
class CaseFileSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "fecha", "hora", "expediente", "tipo", "area_asignada", "prioridad", "nota_inicio", "nota_fin", "aeropuerto", "usuario", "frecuencia", "unidad", "provincia", "localidad", "motivo","domicilio", "latitud", "longitud", "area_actual", "informe", "tramitacion", "status")

case_file_schema = CaseFileSchema()
case_files_schema = CaseFileSchema( many = True )


@bp.route("/file", methods=["POST"])
@auth.login_required
def case_file():
    try:
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        expediente = request.json.get('expediente')
        tipo = request.json.get('tipo')
        area_asignada = request.json.get('area_asignada')
        prioridad = request.json.get('prioridad')
        nota_inicio = request.json.get('nota_inicio')
        nota_fin = request.json.get('nota_fin')
        aeropuerto = request.json.get('aeropuerto')
        usuario = request.json.get('usuario')
        frecuencia = request.json.get('frecuencia')
        unidad = request.json.get('unidad')
        provincia = request.json.get('provincia')
        localidad = request.json.get('localidad')
        motivo = request.json.get('motivo')
        fecha_fin = request.json.get('fecha_fin')
        hora_fin = request.json.get('hora_fin')
        area_actual = request.json.get('area_asignada')
        domicilio = request.json.get('domicilio')
        latitud = request.json.get('latitud')
        longitud = request.json.get('longitud')
        informe = request.json.get('informe')
        tramitacion = 'Pendiente'
        
      
        caseFile = CaseFile(expediente = expediente, area_asignada = area_asignada, fecha = fecha, hora = hora, tipo = tipo, prioridad = prioridad, nota_inicio = nota_inicio, nota_fin = nota_fin, aeropuerto = aeropuerto, usuario = usuario, frecuencia = frecuencia, unidad = unidad, provincia = provincia, localidad = localidad, motivo = motivo, area_actual = area_actual, fecha_fin = fecha_fin, hora_fin = hora_fin, domicilio = domicilio, latitud = latitud, longitud = longitud, informe = informe, tramitacion = tramitacion)
        db.session.add(caseFile)
        db.session.commit()

        usuario = auth.current_user()
        checkUser= User.query.filter_by(usuario=usuario).first()
        stmt1 = (insert(file_tracking).values(file_id = caseFile.id, envia = checkUser.area, recibe = request.json.get('area_asignada'), fecha = request.json.get('fecha'), hora = request.json.get('hora'), usuario = checkUser.usuario))
        session = db.session
        session.execute(stmt1)
        session.commit()

                
        response = {"id": caseFile.id }
        return response, 201 
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400

@bp.route('/file', methods = ['GET'])
@auth.login_required
def get_available_files():
    try:
        include_deleted = request.args.get('includeDeleted')
        file_status = request.args.get('fileStatus')
        usuario = auth.current_user()
        checkUser= User.query.filter_by(usuario = usuario).first()
        if checkUser.area != 'AGCCTYL':
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                case_file_available = CaseFile.query.filter_by(area_actual = checkUser.area)
                if file_status is not None:
                    case_file_available = case_file_available.filter_by(tramitacion = file_status)
                
                case_file_available = case_file_available.all()

            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                case_file_available = CaseFile.query.filter_by(area_actual = checkUser.area, status='Available')
                if file_status is not None:
                    case_file_available = case_file_available.filter_by(tramitacion = file_status)
                
                case_file_available = case_file_available.all()
        else:
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                if file_status is not None:
                    case_file_available = CaseFile.query.filter_by(tramitacion = file_status)
                
                case_file_available = case_file_available.all()
            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                case_file_available = CaseFile.query.filter_by(status='Available')          
                if file_status is not None:
                    case_file_available = case_file_available.filter_by(tramitacion = file_status)
                
                case_file_available = case_file_available.all()

        return case_files_schema.dump(case_file_available)

    except:
        response = {"message": "input error"}
        return response, 400
    
@bp.route('/file/<id>', methods = ['GET'])
@auth.login_required
def get_file(id):
    try:
        caseFile = CaseFile.query.get(id)
        stmt = select(file_tracking).where(file_tracking.c.file_id == id).order_by(file_tracking.c.fecha.desc(), file_tracking.c.hora.desc())
        session = db.session
        result = session.execute(stmt).first()
    
        response = {'file': case_file_schema.dump(caseFile), 'currentArea': result.recibe }
        return response
    except Exception as e:
        print(e)
        response = {"message": "input error"}
        return response, 400


@bp.route('/file/<id>', methods = ['DELETE'])
@auth.login_required
def delete_file(id):
    try:
        case_file = CaseFile.query.get(id)
        case_file.status = 'Deleted'
        stations_in_file = Station.query.filter_by(file_id = id)

        for station in stations_in_file:
            station.status = 'Deleted'

        db.session.commit()
        response = {'id': case_file.id}
        return response

    except:
        response = {"message": "input error"}
        return response, 400


@bp.route('/file/<id>', methods = ['PATCH'])
@auth.login_required
def patch_file(id):
    try:
        caseFile = CaseFile.query.get(id)
        expediente = request.json.get('expediente')
        informe = request.json.get('informe')
        area_destino = request.json.get('area_destino')
        if caseFile and area_destino and caseFile.expediente != 'A definir':
            if area_destino == 'AGCCTYL':
                caseFile.tramitacion = 'Informado'
            else:
                caseFile.tramitacion = 'Pendiente'
            
            caseFile.informe = informe
            caseFile.area_actual = area_destino
            db.session.commit()

            stmt = select(file_tracking).where(file_tracking.c.file_id == id).order_by(file_tracking.c.fecha.desc(), file_tracking.c.hora.desc())
            session = db.session
            currentArea = session.execute(stmt).first()

            usuario = auth.current_user()
            checkUser= User.query.filter_by(usuario = usuario).first()
            stmt1 = (insert(file_tracking).values(file_id = caseFile.id, envia = currentArea.recibe, recibe = area_destino, fecha = request.json.get('fecha'), hora = request.json.get('hora'), usuario = checkUser.usuario))
            session = db.session
            session.execute(stmt1)
            session.commit()

        elif caseFile and caseFile.expediente == 'A definir':         
            caseFile.expediente = expediente
            db.session.commit()

        else:
            return {"error": "id not found/area_destino not valid/not allow action"}, 404

        response = {"id": caseFile.id }
        return response, 201 
    except:
        response = {"message": "input error"}
        return response, 400
