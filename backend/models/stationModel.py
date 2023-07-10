from app import db, app, ma
# defino la clase producto y los tipos de dato de la tabla


class Producto(db.Model):   # la clase Producto hereda de db.Model
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


with app.app_context():
    db.create_all()  # crea las tablas si no estan creadas, sino sigue


#  ************************************************************
class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'precio', 'stock', 'imagen')


producto_schema = ProductoSchema()            # para crear un producto
productos_schema = ProductoSchema(many=True)  # multiples registros
