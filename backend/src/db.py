from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import CheckConstraint
import os
from sqlalchemy.sql import text

# create the extension
db = SQLAlchemy()
ma = Marshmallow()

from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

@event.listens_for(Engine, "connect") #This method gives you an error in case you try to post an invalid foreign key
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

technician_station = db.Table(
    "technician_station",
    db.Model.metadata,
    db.Column("id_station", db.Integer, db.ForeignKey("Station.id")),
    db.Column("id_technician", db.Integer, db.ForeignKey("Technician.id")),
)

technician_tech_measurement = db.Table(
    "technician_tech_measurement",
    db.Model.metadata,
    db.Column("id_tech_measurement", db.Integer, db.ForeignKey("TechMeasurement.id")),
    db.Column("id_technician", db.Integer, db.ForeignKey("Technician.id")),
)

technician_nir = db.Table(
    "technician_nir",
    db.Model.metadata,
    db.Column("id_nir", db.Integer, db.ForeignKey("NonIonizingRadiation.id")),
    db.Column("id_technician", db.Integer, db.ForeignKey("Technician.id")),
)

file_tracking = db.Table(
    "file_tracking",
    # db.Model.metadata,
    db.Column("file_id", db.Integer, db.ForeignKey("File.id")),
    db.Column("envia", db.String),
    db.Column("recibe", db.String),
    db.Column("fecha", db.String),
    db.Column("hora", db.String),
    db.Column("usuario", db.String),
)

# view_file_tracking_status = db.Table(
#     "view_file_tracking_status",
#     db.Model.metadata,
#     db.Column("id", db.Integer),
#     db.Column("tramitacion", db.String),
#     db.Column("status", db.String),
#     db.Column("envia", db.String),
#     db.Column("recibe", db.String),
#     db.Column("fecha", db.String),
#     db.Column("hora", db.String),
#     db.Column("estado", db.String),
#     db.Column("indice_estado", db.Integer),
# )

class CaseFile(db.Model):   # la clase Producto hereda de db.Model
    # define los campos de la tabla
    __tablename__= "File"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(10))
    expediente = db.Column(db.String(50), nullable = False)
    tipo = db.Column(db.String(50))
    area_asignada = db.Column(db.String(25))
    prioridad = db.Column(db.String(10))
    nota_inicio = db.Column(db.String(50))
    nota_fin = db.Column(db.String(50))
    aeropuerto = db.Column(db.String(50))
    frecuencia = db.Column(db.Float, nullable=True)
    unidad = db.Column(db.String(3))
    provincia = db.Column(db.String(30))
    localidad = db.Column(db.String(30))
    usuario = db.Column(db.String(50))
    motivo = db.Column(db.String(300))
    fecha_fin = db.Column(db.String(10))
    hora_fin = db.Column(db.String(10))
    area_actual = db.Column(db.String(25))
    domicilio = db.Column(db.String(50))
    latitud = db.Column(db.Float, nullable=True)
    longitud = db.Column(db.Float, nullable=True)
    informe = db.Column(db.String(50))
    tramitacion = db.Column(db.String(10))
    status = db.Column(db.String(10), nullable=False, default='Available', server_default='Available')
   
    __table_args__ = (
        CheckConstraint("status IN ('Available', 'Deleted')", name='estado_valido'),
    )

    
class Station(db.Model):   # la clase Producto hereda de db.Model
    # define los campos de la tabla
    __tablename__= "Station"
    id = db.Column(db.Integer, primary_key = True)
    file_id = db.Column(db.Integer, db.ForeignKey('File.id'), nullable = False)
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(5))
    area = db.Column(db.String(25))
    identificacion = db.Column(db.String(50), nullable = False)
    emplazamiento = db.Column(db.String(15))
    servicio = db.Column(db.String(6))
    frecuencia = db.Column(db.Float)
    unidad = db.Column(db.String(3))
    claseEmision = db.Column(db.String(5))
    irradiante = db.Column(db.String(30))
    polarizacion = db.Column(db.String(15))
    cantidad = db.Column(db.Integer)
    altura = db.Column(db.Integer)
    tipoVinculo = db.Column(db.String(15))
    frecuenciaVinc =  db.Column(db.Float)
    unidadVinc = db.Column(db.String(3))
    irradianteVinc = db.Column(db.String(10))
    polarizacionVinc = db.Column(db.String(15))
    provincia = db.Column(db.String(30))
    localidad = db.Column(db.String(30))
    domicilio = db.Column(db.String(50))
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    observaciones = db.Column(db.String(300))
    related_station_id = db.Column(db.Integer)
    status = db.Column(db.String(10), nullable=False, default='Available', server_default='Available')
    id_technician1 = db.Column(db.Integer)
    id_technician2 = db.Column(db.Integer)
    technicians = db.orm.relationship("Technician", secondary="technician_station")

class TechMeasurement(db.Model):
    __tablename__= 'TechMeasurement'
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(5))
    puntoMedicion = db.Column(db.String(20))
    station_id = db.Column(db.Integer, db.ForeignKey('Station.id'), nullable = False)
    frecMedida = db.Column(db.Float)
    unidadFrecMedida = db.Column(db.String(3))
    anchoBanda =  db.Column(db.Float)
    unidadBW = db.Column(db.String(3))
    domicilio = db.Column(db.String(50))
    localidad = db.Column(db.String(50))
    provincia = db.Column(db.String(50))
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    distancia = db.Column(db.Float)
    azimut = db.Column(db.Integer)
    observaciones = db.Column(db.String(200))
    domicilioTestigo = db.Column(db.String(50))
    localidadTestigo = db.Column(db.String(50))
    provinciaTestigo = db.Column(db.String(50))
    latitudTestigo = db.Column(db.Float)
    longitudTestigo = db.Column(db.Float)   
    distanciaTestigo = db.Column(db.Float)
    azimutTestigo = db.Column(db.Integer)
    eMedido = db.Column(db.Float)
    eTestigo = db.Column(db.Float)
    eCorregido = db.Column(db.Float)
    incertidumbre = db.Column(db.Float)
    equipamiento = db.Column(db.String(200))
    resultadoComprob = db.Column(db.String(300))
    id_technician1 = db.Column(db.Integer)
    id_technician2 = db.Column(db.Integer)
    status = db.Column(db.String(10), nullable=False, default='Available', server_default='Available')

    
class Technician (db.Model):
    __tablename__ = 'Technician'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre = db.Column(db.String(50), nullable = False)
    apellido = db.Column(db.String(50), nullable = False)
    area = db.Column(db.String(20), nullable = False)
    

class User (db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    usuario = db.Column(db.String(50), unique=True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    area = db.Column(db.String(50), nullable = False)
    perfil = db.Column(db.String(50), nullable = True) ##'coordinator' / 'technician'
    email = db.Column(db.String(50), nullable = False)

class NonIonizingRadiation (db.Model):
    __tablename__ = 'NonIonizingRadiation'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    file_id = db.Column(db.Integer, db.ForeignKey('File.id'), nullable = False)
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(5))
    cantidad = db.Column(db.Integer)
    valor_maximo = db.Column(db.Float)
    observaciones = db.Column(db.String(200))
    id_technician1 = db.Column(db.Integer)
    id_technician2 = db.Column(db.Integer)
    technicians = db.orm.relationship("Technician", secondary="technician_nir")



class Activity (db.Model):
    __tablename__ = 'Activity'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    file_id = db.Column(db.Integer, db.ForeignKey('File.id'), nullable = False)
    fecha = db.Column(db.String(10))
    detalle = db.Column(db.String(500), nullable = False)
    usuario = db.Column(db.String(20))
    
def execute_sql_file(app, file_name):
    # Ruta al archivo SQL
    sql_file_path = os.path.join(os.path.dirname(__file__), 'sql', file_name)
    
    # Leer el contenido del archivo SQL
    try:
        with open(sql_file_path, 'r') as file:
            sql_query = file.read()
        
        # Ejecutar la consulta
        with app.app_context():
            db.session.execute(text(sql_query))
            db.session.commit()
            print("Comando sql ejecutado exitosamente.")
    except Exception as e:
        print(f"Error al ejecutar comando sql: {e}")

def init_app(app):
    print("Estoy entrando!")
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sncte-db.sqlite"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_PATH"] ## Variable de ambiente. Ejecutar: export DB_PATH=sqlite:///sncte-db.sqlite 
    # app.config["SQLALCHEMY_BINDS"] = {'main': 'sqlite:///sncte-db.sqlite'}
    db.init_app(app)
    with app.app_context():
        db.create_all()  # crea las tablas si no estan creadas, sino sigue
        execute_sql_file(app, 'drop_views.sql')
        execute_sql_file(app, 'vista_estado.sql')