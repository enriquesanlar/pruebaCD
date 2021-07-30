from sqlalchemy.orm import backref
from app import db
from dataclasses import dataclass

""" Modelo de la base de datos """

@dataclass
class Estado(db.Model):
    c_estado: int           # Clave de estado
    d_estado: str           # Nombre de estado

    c_estado = db.Column(db.Integer, primary_key=True)
    d_estado = db.Column(db.String(80), nullable=False)
    municipios = db.relationship('Municipio', backref='estado', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.c_estado

@dataclass
class Municipio(db.Model):
    c_mnpio: int            # Clave de municipio
    D_mnpio: str            # Nombre de municipio
    c_estado: int           # Clave de estado


    c_mnpio = db.Column(db.Integer, primary_key=True)
    D_mnpio = db.Column(db.String(80), nullable=False)
    c_estado = db.Column(db.Integer, db.ForeignKey('estado.c_estado'), nullable=False)
    colonias = db.relationship('Colonia', backref='municipio', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.c_mnpio


@dataclass
class Colonia(db.Model):
    id_asenta_cpcons: int   # Identificador de asentamiento
    d_codigo: int           # Código postal asentamiento
    d_asenta: str           # Nombre asentamiento
    c_mnpio: int            # Clave de municipio

    id_asenta_cpcons = db.Column(db.Integer, primary_key=True)
    d_codigo = db.Column(db.Integer, nullable=False)
    d_asenta = db.Column(db.String(80), nullable=False)
    c_mnpio = db.Column(db.Integer, db.ForeignKey('municipio.c_mnpio'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id_asenta_cpcons
