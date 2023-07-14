from flask import Flask , jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import render_template  # incluimos para el renderizado de template
 
app = Flask(__name__)
CORS(app)


#configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/proyectot'
#                  driveBaseDatosMySQL://user:clave@URLBaseDatos/nombreBaseDatos
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db-radiolocalizacion'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
     
from controlers.stationControler import *
# from controladores.controladorUsuarios import *
from models.stationModel import *
# from modelos.modeloUsuarios import *
# print(__name__)  # __nain__
# programa principal
init_app(app)

if __name__=='__main__':  
    app.run(debug=True, port=5000)  # ejecuta la aplicacion en modo debug en el puerto 50000
