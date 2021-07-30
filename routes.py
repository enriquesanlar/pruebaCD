from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from app import db
from model import Municipio, Colonia, Estado
import pandas as pd


@app.route("/colonias", methods=["GET","POST"])
def colonias():
    """
    Colonias por CP. Recibe parámetros en JSON:
        cp - Código postal
    Regresa coincidencias en JSON.
    """
    req = request.get_json()
    res = Colonia.query.filter_by(d_codigo=req['cp']).all()
    return jsonify(res), 200


@app.route("/busqueda", methods=["GET","POST"])
def busqueda():
    """
    Busqueda por nombre. Recibe parámetros en JSON:
        type - Estado, municipio o colonia 
        name - Nombre a buscar
    Regresa coincidencias en JSON.
    """
    req = request.get_json()
    if req['type'] == 'estado':
        res = Estado.query.filter_by(d_estado=req['name']).all()
    elif req['type'] == 'municipio':
        res = Municipio.query.filter_by(D_mnpio=req['name']).all()
    elif req['type'] == 'colonia':
        res = Colonia.query.filter_by(d_asenta=req['name']).all()
    return jsonify(res), 200


@app.route("/agrega", methods=["GET","POST"])
def agrega():
    """
    Busqueda por nombre. Recibe parámetros en JSON:
        type - estado, municipio o colonia 
        data - Datos a agregar como subarreglo
    Respuesta HTTP 200.
    """
    req = request.get_json()
    if req['type'] == 'estado':
        exists = Estado.query.filter_by(c_estado=req['data']['c_estado']).first()
        if not exists:
            edo = Estado(c_estado=req['data']['c_estado'], d_estado=req['data']['d_estado'])
            db.session.add(edo)  
            db.session.commit()
    elif req['type'] == 'municipio':
            exists = Municipio.query.filter_by(c_mnpio=req['data']['c_mnpio']).first()
            if not exists:
                mnp = Municipio(c_mnpio=req['data']['c_mnpio'],D_mnpio=req['data']['D_mnpio'],c_estado=req['data']['c_estado'])
                db.session.add(mnp)  
                db.session.commit()
    elif req['type'] == 'colonia':
            exists = Colonia.query.filter_by(id_asenta_cpcons=req['data']['id_asenta_cpcons']).first()
            if not exists:
                col = Colonia(id_asenta_cpcons=req['data']['id_asenta_cpcons'],d_codigo=req['data']['d_codigo'],d_asenta=req['data']['d_asenta'],c_mnpio=req['data']['c_mnpio'])
                db.session.add(col)
                db.session.commit() 
    return make_response('Hecho'), 200


@app.route('/seed', methods = ['GET','POST'])
def seed():
    """
    Rellena la base de datos desde el archivo CPdescarga.xml
    Recibe parámetros en JSON:
        regs - Número de colonias por municipio
    """
    
    db.drop_all()
    db.create_all()
    xls = pd.ExcelFile("CPdescarga.xls")
    req = request.get_json()
    n_rows = req['regs']

    for j in range(1,33):
        estado = xls.parse(j,nrows=n_rows)
        edo = Estado(c_estado=estado['c_estado'][0], d_estado=estado['d_estado'][0])
        exists = Estado.query.filter_by(c_estado=['c_estado'][0]).first()
        if not exists:
            db.session.add(edo)  
            db.session.commit() 
        for i in range(0,n_rows):
            exists = Municipio.query.filter_by(c_mnpio=estado['c_mnpio'][i]).first()
            if not exists:
                mnp = Municipio(c_mnpio=estado['c_mnpio'][i],D_mnpio=estado['D_mnpio'][i],c_estado=estado['c_estado'][i])
                db.session.add(mnp)
                db.session.commit() 
            exists = Colonia.query.filter_by(id_asenta_cpcons=estado['id_asenta_cpcons'][i]).first()
            if not exists:
                col = Colonia(id_asenta_cpcons=estado['id_asenta_cpcons'][i],d_codigo=estado['d_codigo'][i],d_asenta=estado['d_asenta'][i],c_mnpio=estado['c_mnpio'][i])
                db.session.add(col)
                db.session.commit() 
    return "Hecho.", 200