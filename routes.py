from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from app import db
from model import Municipio, Colonia, Estado


@app.route("/colonias", methods=["GET"])
def colonias():
    """
    Colonias por CP. Recibe parámetros en JSON:
        cp - Código postal
    Regresa coincidencias en JSON.
    """

    return 'cp'


@app.route("/busqueda", methods=["GET"])
def busqueda():
    """
    Busqueda por nombre. Recibe parámetros en JSON:
        type - Estado, municipio o colonia 
        name - Nombre a buscar
    Regresa coincidencias en JSON.
    """
    return make_response(1)

@app.route("/agrega", methods=["GET"])
def agrega():
    """
    Busqueda por nombre. Recibe parámetros en JSON:
        type - Estado, municipio o colonia 
        name - Nombre a buscar
    Respuesta HTTP 200.
    """
    return make_response(1)