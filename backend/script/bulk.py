import csv
from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker
from src.db import CaseFile, file_tracking, User  # Ajusta según tu estructura de proyecto

# Configuración de la conexión a la base de datos
DATABASE_URL = "sqlite:///../instance/sncte-db.sqlite"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def bulk_upload(csv_file):
    try:
        # Leer el archivo CSV
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_data = csv.DictReader(file, delimiter =';')
            
            case_files = []
            file_trackings = []

            # Suponiendo que estás simulando un usuario específico
            usuario_id = 1  # Reemplaza con un ID válido
            checkUser = session.query(User).filter_by(id=usuario_id).first()

            for row in csv_data:
                # print(f"Procesando fila: {row}")
                expediente = row.get('expediente')
                print('frecuencia', row.get('frecuencia'))
                print('latitud', row.get('latitud'))
                print("Row: ",row)  
                #               # Crear una instancia de CaseFile
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
                    provincia=row.get('provincia'),
                    localidad=row.get('localidad'),
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
                session.commit()


                # Preparar el tracking asociado
                tracking = {
                    "file_id": None,  # Se asignará después de guardar case_files
                    "envia": checkUser.area,
                    "recibe": row.get('area_asignada'),
                    "fecha": row.get('fecha'),
                    "hora": row.get('hora'),
                    "usuario": checkUser.usuario
                }
                file_trackings.append(tracking)

            # Insertar CaseFile en la base de datos
            session.bulk_save_objects(case_files)
            session.commit()

            # Asignar IDs generados a los trackings
            for i, caseFile in enumerate(case_files):
                # import pdb; pdb.set_trace()
                file_trackings[i]["file_id"] = caseFile.id

            # Insertar tracking
            stmt = file_tracking.insert().values(file_trackings)
            session.execute(stmt)
            session.commit()

            print(f"{len(case_files)} expedientes cargados correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

# Ejecutar el script
csv_file = 'exported-files.csv'
bulk_upload(csv_file)
