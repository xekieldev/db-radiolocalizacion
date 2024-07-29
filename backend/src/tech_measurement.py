from flask import Blueprint
from src.db import ma

bp = Blueprint("tech_measurement", __name__)

class TechMeasurementSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "fecha", "hora", "puntoMedicion", "station_id", "frecMedida", "unidadFrecMedida", "anchoBanda",
                   "unidadBW", "domicilio", "localidad", "provincia", "latitud", "longitud", "distancia",
                     "azimut", "observaciones", "domicilioTestigo", "localidadTestigo", "provinciaTestigo", 
                       "latitudTestigo", "longitudTestigo", "distanciaTestigo", "azimutTestigo", "eMedido", 
                       "eTestigo", "eCorregido","incertidumbre","equipamiento", "resultadoComprob", "id_technician1", "id_technician2", "status")

tech_measurement_schema = TechMeasurementSchema()
tech_measurements_schema = TechMeasurementSchema( many = True )

    



