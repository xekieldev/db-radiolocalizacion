from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

# create the extension
db = SQLAlchemy()
ma = Marshmallow()

technician_file = db.Table(
    "technician_file",
    db.Model.metadata,
    db.Column("id_file", db.Integer, db.ForeignKey("File.id")),
    db.Column("id_technician", db.Integer, db.ForeignKey("Technician.id")),
)

class Filex(db.Model):   # la clase Producto hereda de db.Model
    # define los campos de la tabla
    __tablename__= "File"
    id = db.Column(db.Integer, primary_key = True)
    expediente = db.Column(db.String(50), nullable = False)
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(5))
    area = db.Column(db.String(20))
    # id_station = db.Column(db.Integer, db.ForeignKey('Station.id'), nullable = False)
    # stations = db.relationship('Station', backref='file', lazy = True)
    # id_technician1 = db.Column(db.Integer, db.ForeignKey('Technician.id'), nullable = False)
    # id_technician2 = db.Column(db.Integer, db.ForeignKey('Technician.id'), nullable = False)
    # technicians = db.relationship('Technician', backref='file', lazy = True)
    technicians = db.orm.relationship("Technician", secondary="technician_file")
    
class Station(db.Model):   # la clase Producto hereda de db.Model
    # define los campos de la tabla
    __tablename__= "Station"
    id = db.Column(db.Integer, primary_key = True)
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
    # id_location = db.Column(db.Integer, db.ForeignKey('Location.id'), nullable = False)
    # locations = db.relationship('Location', backref = 'station', lazy = True)
    location = db.orm.relationship("Location")
    id_location = db.Column(db.Integer, db.ForeignKey("Location.id"))


    
class Location(db.Model):   # la clase Producto hereda de db.Model
    # define los campos de la tabla
    __tablename__= "Location"
    id = db.Column(db.Integer, primary_key = True)
    provincia = db.Column(db.String(30))
    localidad = db.Column(db.String(30))
    domicilio = db.Column(db.String(50))
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    observaciones = db.Column(db.String(300))

class TechMeasurement(db.Model):
    __tablename__= 'TechMeasurement'
    id = db.Column(db.Integer, primary_key = True)
    id_file = db.Column(db.Integer, db.ForeignKey('File.id'), nullable = False)
    # files = db.relationship('File', backref = 'TechMeasurements', lazy = True)
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(5))
    area = db.Column(db.String(20))
    id_location = db.Column(db.Integer, db.ForeignKey('Location.id'), nullable = False)
    # locations = db.relationship('Location', backref = 'tecnMeasurements', lazy = True)
    distancia = db.Column(db.Float)
    azimut = db.Column(db.Integer)
    mic = db.Column(db.Float)
    claseEmision = db.Column(db.String(5))
    anchoBanda =  db.Column(db.Float)
    unidad = db.Column(db.String(3))
    noEsencial1 = db.Column(db.Float)
    micNoEsencial1 = db.Column(db.Float)
    noEsencial2 = db.Column(db.Float)
    micNoEsencial2 = db.Column(db.Float)
    noEsencial3 = db.Column(db.Float)
    micNoEsencial3 = db.Column(db.Float)
    resultadoComprob = db.Column(db.String(300))
    id_technician = db.Column(db.Integer, db.ForeignKey('Technician.id'), nullable = False)
    # technicians = db.relationship('Technician', backref='file', lazy = True)


class Technician (db.Model):
    __tablename__ = 'Technician'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre = db.Column(db.String(50), nullable = False)
    apellido = db.Column(db.String(50), nullable = False)
    


# #  ************************************************************
# class StationSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'nombre', 'precio', 'stock', 'imagen')


# station_schema = StationSchema()            # para crear un producto
# stations_schema = StationSchema(many=True)  # multiples registros

def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///radioloc.sqlite"
    db.init_app(app)
    with app.app_context():
        db.create_all()  # crea las tablas si no estan creadas, sino sigue
