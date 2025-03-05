from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask import request,  jsonify
from src.db import db, CaseFile, Station, TechMeasurement, technician_tech_measurement, technician_station, Technician, file_tracking, ma, User
from sqlalchemy import exc, insert, delete, select, update, func
from src.technician import technicians_schema
from src.station import station_schema, stations_schema
from src.non_ionizing_radiation import delete_nir
from src.tech_measurement import tech_measurements_schema, tech_measurement_schema
# from src.users import auth
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from sqlalchemy import and_, func, or_
from sqlalchemy.orm import aliased
from datetime import datetime
from datetime import date


temp_db = SQLAlchemy()

view_file_tracking_status = temp_db.Table(
    "view_file_tracking_status",
    temp_db.Model.metadata,
    temp_db.Column("id", temp_db.Integer),
    temp_db.Column("tramitacion", temp_db.String),
    temp_db.Column("tipo", temp_db.String),
    temp_db.Column("area_asignada", temp_db.String),
    temp_db.Column("status", temp_db.String),
    temp_db.Column("envia", temp_db.String),
    temp_db.Column("recibe", temp_db.String),
    temp_db.Column("fecha", temp_db.String),
    temp_db.Column("hora", temp_db.String),
    temp_db.Column("estado", temp_db.String),
    temp_db.Column("indice_estado", temp_db.Integer),
)

bp = Blueprint("case_file", __name__)
class CaseFileSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "fecha", "hora", "expediente", "tipo", "area_asignada", "prioridad", "nota_inicio", "nota_fin", "aeropuerto", "usuario", "frecuencia", "unidad", "provincia", "localidad", "motivo","domicilio", "latitud", "longitud", "area_actual", "informe", "tramitacion", "status")

case_file_schema = CaseFileSchema()
case_files_schema = CaseFileSchema( many = True )


class ViewSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "status", "tipo", "area_asignada", "envia", "recibe", "fecha", "hora", "estado", "indice_estado")

view_schema = ViewSchema()
views_schema = ViewSchema( many = True )

@bp.route("/file", methods=["POST"])
@jwt_required()
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

        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
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

@bp.route("/file/<id>", methods=["PUT"])
@jwt_required()
def edit_file(id):
    try:
        caseFile = CaseFile.query.get(id)
        if caseFile:    
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

            if caseFile.tramitacion == 'Pendiente' and (fecha != caseFile.fecha or hora != caseFile.hora or area_asignada != caseFile.area_asignada):
                usuario_id = get_jwt_identity()
                checkUser = User.query.filter_by(id=usuario_id).first()
                stmt_update = (update(file_tracking).where(file_tracking.c.file_id == caseFile.id).values(
                    fecha=fecha,
                    hora=hora,
                    envia=checkUser.area,
                    recibe=area_asignada,
                    usuario=checkUser.usuario
                    )
                )
                db.session.execute(stmt_update)

            caseFile.fecha = fecha
            caseFile.hora = hora
            caseFile.expediente = expediente
            caseFile.tipo = tipo
            caseFile.area_asignada = area_asignada
            caseFile.prioridad = prioridad
            caseFile.nota_inicio = nota_inicio
            caseFile.nota_fin = nota_fin
            caseFile.aeropuerto = aeropuerto
            caseFile.usuario = usuario
            caseFile.frecuencia = frecuencia
            caseFile.unidad = unidad
            caseFile.provincia = provincia
            caseFile.localidad = localidad
            caseFile.motivo = motivo
            caseFile.fecha_fin = fecha_fin
            caseFile.hora_fin = hora_fin
            caseFile.area_actual = area_actual
            caseFile.domicilio = domicilio
            caseFile.latitud = latitud
            caseFile.longitud = longitud
            caseFile.informe = informe
        
        
            db.session.commit()   
            response = {"id": caseFile.id }
            return response, 201 
        else:
            return {"error": "id not found"}, 404        
    except exc.SQLAlchemyError:
        response = { "message": "database error" }
        return response, 500
    except:
        response = { "message": "input error" }
        return response, 400

@bp.route('/file', methods = ['GET'])
@jwt_required()
def get_available_files():
    try:
        include_deleted = request.args.get('includeDeleted')
        file_status = request.args.get('fileStatus')
        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        if checkUser.area != 'AGCCTYL':
            if include_deleted and include_deleted.lower() == 'true':
                # Si includeDeleted está presente y es 'true', lista todos los archivos, incluidos los eliminados
                case_file_available = CaseFile.query.filter_by(area_actual = checkUser.area)
                if file_status is not None:
                    case_file_available = case_file_available.filter_by(tramitacion = file_status)
                
                case_file_available = case_file_available.all()

            else:
                # Si no se proporciona o es diferente de 'true', lista solo los archivos disponibles
                case_file_available = CaseFile.query.filter_by(area_asignada = checkUser.area, status='Available')
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
@jwt_required()
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
@jwt_required()
def delete_file(id):
    try:
        
        case_file = CaseFile.query.get(id)
        case_file.status = 'Deleted'
        stations_in_file = Station.query.filter_by(file_id = id)
        for station in stations_in_file:
            station.status = 'Deleted'
        if case_file.tipo == 'Medición de Radiaciones No Ionizantes (móviles)':
            delete_nir(id)
        db.session.commit()
        response = {'id': case_file.id, 'status': 200}

        return response, 200

    except:
        response = {"message": "input error"}
        return response, 400


@bp.route('/file/<id>', methods=['PATCH'])
@jwt_required()
def patch_file(id):
    try:
        caseFile = CaseFile.query.get(id)
        expediente = request.json.get('expediente')
        informe = request.json.get('informe')
        area_destino = request.json.get('area_destino')

        if caseFile and area_destino and caseFile.expediente != 'A definir':
            usuario_id = get_jwt_identity()
            checkUser = User.query.filter_by(id=usuario_id).first()
            session = db.session
            
            # Si es "Descargo" y el destino es "Guarda Temporal", ejecutamos dos veces
            area_destinos = ['AGCCTYL', 'Guarda Temporal'] if caseFile.tipo == 'Descargo' and area_destino == 'Guarda Temporal' else [area_destino]

            for i, destino in enumerate(area_destinos):
                if destino == 'AGCCTYL':
                    caseFile.tramitacion = 'Informado'
                    caseFile.informe = informe
                elif destino != caseFile.area_asignada:
                    caseFile.tramitacion = 'Finalizado'
                    caseFile.fecha_fin = datetime.today().strftime('%Y-%m-%d')
                    caseFile.hora_fin = datetime.today().strftime('%H:%M')
                    if caseFile.tipo == 'Interferencias en Aeropuertos':
                        caseFile.nota_fin = request.json.get('nota_fin')
                else:
                    caseFile.tramitacion = 'Pendiente'

                caseFile.area_actual = destino
                session.commit()

                if i == 0:
                    session.refresh(caseFile)  # Refresca los valores en SQLAlchemy

                stmt = select(file_tracking).where(file_tracking.c.file_id == id).order_by(file_tracking.c.fecha.desc(), file_tracking.c.hora.desc())
                currentArea = session.execute(stmt).first()

                stmt1 = insert(file_tracking).values(
                    file_id=caseFile.id,
                    envia=currentArea.recibe if currentArea else None, 
                    recibe=destino,
                    fecha=request.json.get('fecha'),
                    hora=request.json.get('hora'),
                    usuario=checkUser.usuario
                )
                session.execute(stmt1)
                session.commit()

        elif caseFile and caseFile.expediente == 'A definir':
            caseFile.expediente = expediente
            db.session.commit()
        else:
            return {"error": "id not found/area_destino not valid/not allow action"}, 404

        return {"id": caseFile.id}, 201

    except Exception as e:
        print(f"Error: {e}") 
        return {"message": "input error"}, 400

@bp.route('/statistics', methods = ['GET'])
@jwt_required()
def statistics():
    try:
        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        # if checkUser.area != 'AGCCTYL':  
        case_file_available = CaseFile.query.filter_by(status='Available')      


        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        type = request.args.get('type')
        selected_area = request.args.get('area')

        if start_date is None:
            start_date = '2000-01-01'
        if end_date is None:
            end_date = date.today()

        if type == 'inbound':
            filtered_files = case_file_available.filter(CaseFile.fecha >= start_date, CaseFile.fecha <= end_date )
            return case_files_schema.dump(filtered_files)
        else:
            vfts = view_file_tracking_status
            condition = vfts.c.estado == type
  
            if type == 'pending':
                # Subconsulta para calcular el estado mínimo (CTE en SQL)
                current_states = (
                    select(
                        vfts.c.id.label("id"),
                        func.min(vfts.c.indice_estado).label("current_indice_estado")
                    )
                    .where(
                        vfts.c.fecha >= start_date,
                        vfts.c.fecha <= end_date
                    )
                    .group_by(vfts.c.id)
                    .subquery("current_states")
                )

                # Consulta principal
                query = (
                    select(vfts)
                    .join(
                        current_states,
                        and_(
                            vfts.c.id == current_states.c.id,
                            vfts.c.indice_estado == current_states.c.current_indice_estado
                        )
                    )
                    .where(condition)
                )
            else:
                query = (
                    select(vfts)
                    .where(
                        and_(
                            vfts.c.estado == type,
                            vfts.c.fecha >= start_date,
                            vfts.c.fecha <= end_date
                        )
                    )
                )
            # print("query", query)
            session = db.session
            result = session.execute(query)
            session.commit()
            return views_schema.dump(result)

    except:
        response = {"message": "input error"}
        return response, 400
        