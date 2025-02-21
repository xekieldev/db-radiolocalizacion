import csv
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from src.db import CaseFile, file_tracking, User  # Ajusta según tu estructura de proyecto

# Cargar datos de provincias y localidades desde JSON
with open("../../frontend/data/provincias.json", "r", encoding="utf-8") as file:
    provinces_data = json.load(file)["provincias"]

with open("../../frontend/data/localidades.json", "r", encoding="utf-8") as file:
    cities_data = json.load(file)["localidades"]

# Crear diccionarios para buscar códigos por nombre
province_name_to_id = {p["nombre"].upper(): p["id"] for p in provinces_data}
city_name_to_id = {c["nombre"].upper(): c["id"] for c in cities_data}

# Función para obtener código desde el nombre
def get_code_by_name(kind, name):
    if not name:  # Evitar errores si el nombre es None o vacío
        return None
    name = name.upper()  # Convertir a mayúsculas para coincidencia
    data = city_name_to_id if kind == "city" else province_name_to_id
    return data.get(name, None)  # Retorna el código o None si no existe

def format_date(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return None  # Si el formato es incorrecto, devolvemos None


# Configuración de la conexión a la base de datos
DATABASE_URL = "sqlite:///../instance/sncte-db.sqlite"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def bulk_upload(csv_file):
    try:
        # Leer el archivo CSV
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_data = csv.DictReader(file, delimiter=',')

            case_files = []
            file_trackings = []

            # Obtener usuario de prueba
            usuario_id = 1  # Reemplazar con un ID válido
            checkUser = session.query(User).filter_by(id=usuario_id).first()
            if not checkUser:
                print("Error: Usuario no encontrado.")
                return

            for row in csv_data:
                # Convertir nombres en códigos
                provincia_codigo = get_code_by_name("province", row.get("provincia"))
                localidad_codigo = get_code_by_name("city", row.get("localidad"))
                print('frecuencia', row.get('frecuencia'))
                print('latitud', row.get('latitud'))
                print("Row: ",row)

                # Crear CaseFile
                caseFile = CaseFile(
                    expediente=row.get('expediente'),
                    area_asignada=row.get('area_asignada'),
                    fecha=row.get('fecha'),
                    hora=row.get('hora'),
                    tipo=row.get('tipo'),
                    prioridad=row.get('prioridad'),
                    nota_inicio=row.get('nota_inicio'),
                    nota_fin=row.get('nota_fin'),
                    aeropuerto=row.get('aeropuerto'),
                    usuario=row.get('usuario'),
                    frecuencia=float(row.get('frecuencia')) if row.get('frecuencia') != 'NULL' else 0,
                    unidad=row.get('unidad'),
                    provincia=provincia_codigo,  # Guardamos el código
                    localidad=localidad_codigo,  # Guardamos el código
                    motivo=row.get('motivo'),
                    area_actual=row.get('area_asignada'),
                    fecha_fin=row.get('fecha_fin'),
                    hora_fin=row.get('hora_fin'),
                    domicilio=row.get('domicilio'),
                    latitud=float(row.get('latitud')) if row.get('latitud') != 'NULL' else 0,
                    longitud=float(row.get('longitud')) if row.get('longitud') != 'NULL' else 0,
                    informe=row.get('informe'),
                    tramitacion='Pendiente',
                )
                case_files.append(caseFile)
                session.add(caseFile)

                # Tracking
                tracking = {
                    "file_id": None,  # Se asignará después de guardar CaseFiles
                    "envia": checkUser.area,
                    "recibe": row.get('area_asignada'),
                    "fecha": row.get('fecha'), #"fecha": format_date(row.get('fecha')),
                    "hora": row.get('hora'),
                    "usuario": checkUser.usuario
                }
                file_trackings.append(tracking)

            # Guardar expedientes en la base de datos
            session.commit()

            # Asignar los IDs generados a los trackings
            for i, caseFile in enumerate(case_files):
                file_trackings[i]["file_id"] = caseFile.id

            # Insertar tracking en la base de datos
            stmt = file_tracking.insert().values(file_trackings)
            session.execute(stmt)
            session.commit()

            print(f"{len(case_files)} expedientes cargados correctamente con tracking.")
    except Exception as e:
        session.rollback()
        print(f"Error en bulk_upload: {e}")
    finally:
        session.close()

# Ejecutar el script
csv_file = 'BA2021-libre.csv'
bulk_upload(csv_file)
