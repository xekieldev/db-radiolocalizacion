from flask import jsonify, request
from app import *
from models.stationModel import *


@app.route('/stations', methods=['GET'])
def get_Stations():
    all_stations = Producto.query.all()
    result = stations_schema.dump(all_stations)
    return jsonify(result)


@app.route('/stations/<id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get(id)
    return producto_schema.jsonify(producto)


@app.route('/stations/<id>', methods=['PUT'])
def update_producto(id):
    producto = Producto.query.get(id)
    nombre = request.json['nombre']  # trae el valor de la clave nombre
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    # update_product_db(nombre, precio, stock, imagen): Propuesta para llevar la escritura de la DB a una función.
    producto.nombre = nombre   # crea un objeto producto
    producto.precio = precio
    producto.stock = stock
    producto.imagen = imagen
    db.session.commit()
    # el objeto producto los convierte a JSON
    return producto_schema.jsonify(producto)


@app.route('/stations/<id>', methods=['DELETE'])
def delete_producto(id):
    producto = Producto.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return producto_schema.jsonify(producto)


@app.route('/stations', methods=['POST'])  # crea ruta o endpoint
def create_producto():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre = request.json['nombre']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    new_producto = Producto(nombre, precio, stock, imagen)
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.jsonify(new_producto)
