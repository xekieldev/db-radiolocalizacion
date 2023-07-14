from flask import jsonify, request
from app import *
from models.stationModel import *


@app.route('/stations', methods=['GET'])
def get_Stations():
    all_stations = Station.query.all()
    result = stations_schema.dump(all_stations)
    return jsonify(result)


@app.route('/stations/<id>', methods=['GET'])
def get_station(id):
    station = Station.query.get(id)
    return station_schema.jsonify(station)


@app.route('/stations/<id>', methods=['PUT'])
def update_station(id):
    station = Station.query.get(id)
    nombre = request.json['nombre']  # trae el valor de la clave nombre
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    # update_product_db(nombre, precio, stock, imagen): Propuesta para llevar la escritura de la DB a una función.
    station.nombre = nombre   # crea un objeto station
    station.precio = precio
    station.stock = stock
    station.imagen = imagen
    db.session.commit()
    # el objeto station los convierte a JSON
    return station_schema.jsonify(station)


@app.route('/stations/<id>', methods=['DELETE'])
def delete_station(id):
    station = Station.query.get(id)
    db.session.delete(station)
    db.session.commit()
    return station_schema.jsonify(station)


@app.route('/stations', methods=['POST'])  # crea ruta o endpoint
def create_station():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre = request.json['nombre']
    precio = request.json['precio']
    stock = request.json['stock']
    imagen = request.json['imagen']
    new_station = Station(nombre, precio, stock, imagen)
    db.session.add(new_station)
    db.session.commit()
    return station_schema.jsonify(new_station)
