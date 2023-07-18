from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

class Station(db.Model):   # la clase Producto hereda de db.Model
    # define los campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    expediente = db.Column(db.String(50))
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(5))
    area = db.Column(db.String(20))

    def __init__(self, expediente, fecha, hora, area):  # crea el  constructor de la clase
        # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.expediente = expediente
        self.fecha = fecha
        self.hora = hora
        self.area = area





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
