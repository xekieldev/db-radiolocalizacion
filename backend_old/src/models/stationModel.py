from app import db, ma
# defino la clase producto y los tipos de dato de la tabla


class Station(db.Model):   # la clase Producto hereda de db.Model
    # define los campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(100))

    def __init__(self, nombre, precio, stock, imagen):  # crea el  constructor de la clase
        # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen





#  ************************************************************
class StationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'precio', 'stock', 'imagen')


station_schema = StationSchema()            # para crear un producto
stations_schema = StationSchema(many=True)  # multiples registros


def init_app(app):
    with app.app_context():
        db.create_all()  # crea las tablas si no estan creadas, sino sigue