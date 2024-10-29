from flask import Blueprint
from flask import request,  jsonify
from src.db import db, CaseFile, Station, TechMeasurement, technician_tech_measurement, technician_station, Technician, file_tracking, ma, User
from sqlalchemy import exc, insert, delete, select
from src.technician import technicians_schema
from src.station import station_schema, stations_schema
from src.tech_measurement import tech_measurements_schema, tech_measurement_schema
# from src.users import auth
from flask_jwt_extended import jwt_required, get_jwt_identity, current_user
from sqlalchemy import and_, func, or_
from sqlalchemy.orm import aliased


bp = Blueprint("case_file", __name__)
class CaseFileSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "fecha", "hora", "expediente", "tipo", "area_asignada", "prioridad", "nota_inicio", "nota_fin", "aeropuerto", "usuario", "frecuencia", "unidad", "provincia", "localidad", "motivo","domicilio", "latitud", "longitud", "area_actual", "informe", "tramitacion", "status")

case_file_schema = CaseFileSchema()
case_files_schema = CaseFileSchema( many = True )


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
            tramitacion = 'Pendiente'

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
            caseFile.tramitacion = tramitacion
        
        
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

        db.session.commit()
        response = {'id': case_file.id, 'status': 200}

        return response, 200

    except:
        response = {"message": "input error"}
        return response, 400


@bp.route('/file/<id>', methods = ['PATCH'])
@jwt_required()
def patch_file(id):
    try:
        caseFile = CaseFile.query.get(id)
        expediente = request.json.get('expediente')
        informe = request.json.get('informe')
        area_destino = request.json.get('area_destino')
        if caseFile and area_destino and caseFile.expediente != 'A definir':
            if area_destino == 'AGCCTYL':
                caseFile.tramitacion = 'Informado'
            elif area_destino != caseFile.area_asignada:
                caseFile.tramitacion = 'Finalizado'
            else:
                caseFile.tramitacion = 'Pendiente'
            
            caseFile.informe = informe
            caseFile.area_actual = area_destino
            db.session.commit()

            stmt = select(file_tracking).where(file_tracking.c.file_id == id).order_by(file_tracking.c.fecha.desc(), file_tracking.c.hora.desc())
            session = db.session
            currentArea = session.execute(stmt).first()

            usuario_id = get_jwt_identity()      
            checkUser= User.query.filter_by(id = usuario_id).first()
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

@bp.route('/statistics', methods = ['GET'])
@jwt_required()
def statistics():
    case_file_data = aliased(CaseFile)
    case_file_track = aliased(file_tracking)
    try:
        file_status = 'Pendiente'
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        type = request.args.get('type')
        selected_area = request.args.get('area')
        usuario_id = get_jwt_identity()      
        checkUser= User.query.filter_by(id = usuario_id).first()
        # if checkUser.area != 'AGCCTYL':  
        response_by_area = []
        response_by_type = []
        case_file_available = CaseFile.query.filter_by(status='Available')      
        areas = ['Buenos Aires', 'Lima', 'Córdoba', 'Salta', 'Posadas', 'Neuquén', 'Comodoro Rivadavia']
        types= ['Interferencias en Aeropuertos',
                'Interferencias en Estaciones Radioeléctricas',
                'Interferencias en Estaciones de Radiodifusión',
                'Interferencias Celulares',
                'Inspección de Estaciones Radioeléctricas',
                'Inspección de Estaciones de Radiodifusión',
                'Radiolocalización de Estaciones Radioeléctricas',
                'Radiolocalización de Estaciones de Radiodifusión',
                'Detectar actividad',
                'Denuncias del Público en general',
                'Medición de Radiaciones No Ionizantes',
                'Otros',
                'Medición de Radiaciones No Ionizantes (móviles)',
                'Descargo']
        if start_date == '' and end_date == '':
            start_date = None
            end_date = None
        # Ingesados
        if type == 'inbound':
            if start_date == None and end_date == None:
                for area in areas:
                    stat_by_area = case_file_available.filter_by(area_asignada= area).count() 
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})
                for type in types:
                    if selected_area == None:
                        stat_by_type = case_file_available.filter_by(tipo= type).count()
                    else:
                        stat_by_type = case_file_available.filter_by(tipo= type, area_asignada = selected_area).count()
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})
            elif start_date == None and end_date != None:
                case_file_available = case_file_available.filter(CaseFile.fecha <= end_date)
                for area in areas:
                    stat_by_area = case_file_available.filter_by(area_asignada= area).count() 
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})
                for type in types:
                    if selected_area == None:
                        stat_by_type = case_file_available.filter_by(tipo= type).count()
                    else:
                        stat_by_type = case_file_available.filter_by(tipo= type, area_asignada = selected_area).count()
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})
            else:
                case_file_available = case_file_available.filter(CaseFile.fecha >= start_date, CaseFile.fecha <= end_date)
                for area in areas:
                    stat_by_area = case_file_available.filter_by(area_asignada= area).count()
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})
                for type in types:
                    if selected_area == None:
                        stat_by_type = case_file_available.filter_by(tipo= type).count()
                    else:
                        stat_by_type = case_file_available.filter_by(tipo= type, area_asignada = selected_area).count()
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})            
            
            return {'Area': response_by_area, 'Tipo': response_by_type}
        # Egresados
        if type =='outbound':
            file_status = 'Informado'
            if start_date == None and end_date == None:

                for area in areas:
                    stat_by_area = case_file_available.filter_by(tramitacion = file_status, area_asignada = area).count() 
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})
                for type in types:
                    if selected_area == None:
                        stat_by_type = case_file_available.filter_by(tramitacion = file_status, tipo = type).count()
                    else:
                        stat_by_type = case_file_available.filter_by(tramitacion = file_status, tipo = type, area_asignada = selected_area).count()
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})
            elif start_date == None and end_date != None:
                case_file_available = (
                    db.session.query(
                        case_file_data,
                        func.max(case_file_track.c.fecha).label("fecha_informe")  # Obtenemos la fecha más reciente del tracking
                    )
                    .join(case_file_track, case_file_data.id == case_file_track.c.file_id)
                    .filter(
                        case_file_data.tramitacion == file_status,  # Filtro de estado
                        case_file_track.c.fecha <= end_date  # Filtro de fecha de fin
                    )
                    .group_by(case_file_data.id, case_file_data.tramitacion, case_file_data.fecha)  # Agrupamos por los campos relevantes
                )
                for area in areas:
                    stat_by_area = case_file_available.filter(case_file_data.area_asignada == area).count()
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})

                for type in types:
                    stat_by_type = case_file_available.filter(case_file_data.tipo == type).count()
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})
            else:
                case_file_available = (
                    db.session.query(
                        case_file_data,
                        func.max(case_file_track.c.fecha).label("fecha_informe")  # Obtenemos la fecha más reciente del tracking
                    )
                    .join(case_file_track, case_file_data.id == case_file_track.c.file_id)
                    .filter(
                        case_file_data.tramitacion == file_status,  # Filtro de estado
                        case_file_data.fecha >= start_date,  # Filtro de fecha de inicio
                        case_file_track.c.fecha <= end_date  # Filtro de fecha de fin
                    )
                    .group_by(case_file_data.id, case_file_data.tramitacion, case_file_data.fecha)  # Agrupamos por los campos relevantes
                )

                for area in areas:
                    stat_by_area = case_file_available.filter(case_file_data.area_asignada == area).count()
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})

                for type in types:
                    stat_by_type = case_file_available.filter(case_file_data.tipo == type).count()
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})
                        
            return {'Area': response_by_area, 'Tipo': response_by_type}
        # Pendientes
        if type == 'pending':
            if start_date == None and end_date == None:
                for area in areas:
                    stat_by_area = case_file_available.filter_by(tramitacion = file_status, area_asignada= area).count() 
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})
                for type in types:
                    if selected_area == None:
                        stat_by_type = case_file_available.filter_by(tramitacion = file_status, tipo = type).count()
                    else:
                        stat_by_type = case_file_available.filter_by(tramitacion = file_status, tipo = type, area_asignada = selected_area).count()
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})
            elif start_date is None and end_date is not None:
                # Subconsulta de expedientes que cumplen con la fecha de ingreso y condiciones de tramitación
                case_file_available = (
                    db.session.query(
                        CaseFile.id,
                        CaseFile.fecha.label("fecha_ingreso"),
                        CaseFile.tramitacion,
                        func.max(file_tracking.c.fecha).label("fecha_informe"),
                        CaseFile.area_asignada,
                        CaseFile.tipo
                    )
                    .outerjoin(file_tracking, CaseFile.id == file_tracking.c.file_id)
                    .filter(
                        CaseFile.fecha <= end_date  # Incluir solo expedientes con fecha de ingreso <= end_date
                    )
                    .group_by(CaseFile.id, CaseFile.fecha, CaseFile.tramitacion, CaseFile.area_asignada, CaseFile.tipo)
                    .having(
                        # Excluir expedientes en estado "Informado" con fecha de informe <= end_date
                        ~((CaseFile.tramitacion == 'Informado') & (func.max(file_tracking.c.fecha) <= end_date))
                    )
                    .subquery(name="case_file_available")
                )

                # Inicialización de las listas de respuesta
                response_by_area = []
                response_by_type = []

                # Conteo por área
                for area in areas:
                    stat_by_area = (
                        db.session.query(case_file_available.c.id)
                        .filter(case_file_available.c.area_asignada == area)
                        .count()
                    )
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})

                # Conteo por tipo, con o sin área seleccionada
                for type in types:
                    if selected_area is None:
                        # Conteo solo por tipo
                        stat_by_type = (
                            db.session.query(case_file_available.c.id)
                            .filter(case_file_available.c.tipo == type)
                            .count()
                        )
                    else:
                        # Conteo por tipo y área
                        stat_by_type = (
                            db.session.query(case_file_available.c.id)
                            .filter(case_file_available.c.tipo == type, case_file_available.c.area_asignada == selected_area)
                            .count()
                        )
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})

                # Retorno de resultados
                return {'Area': response_by_area, 'Tipo': response_by_type}

            else:
                case_file_available = case_file_available.filter(CaseFile.fecha >= start_date, CaseFile.fecha <= end_date)
                for area in areas:
                    stat_by_area = case_file_available.filter_by(tramitacion = file_status, area_asignada= area).count()
                    response_by_area.append({'area': area, 'cantidad': stat_by_area})

                for type in types:
                    stat_by_type = case_file_available.filter_by(tramitacion = file_status, tipo= type).count()
                    response_by_type.append({'tipo': type, 'cantidad': stat_by_type})
            
            return {'Area': response_by_area, 'Tipo': response_by_type}
        return {"message": "No se seleccionó ningún tipo de filtro válido"}, 400
    except:
        response = {"message": "input error"}
        return response, 400