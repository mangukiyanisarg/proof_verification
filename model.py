import datetime
import json, requests
from sqlalchemy import and_

from app import app,  db, STATUS

# Model Class

# class Config(db.Model):
#     """Config Table"""
#     __tablename__ = "tb_config"
#     seq_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     id_type = db.Column(db.String(1000), nullable=False)
#     id_version = db.Column(db.Integer, nullable=False)
#     id_params = db.Column(db.Text, nullable=True)
#     status = db.Column(db.String(1), nullable=False, default=STATUS["ACTIVE"])
#     created_date = db.Column(db.DateTime, nullable=True)
#     updated_date = db.Column(db.DateTime, nullable=True)

#     def __init__(self,id_type,id_params):
#         self.id_type = id_type
#         self.id_params = id_params
#         self.created_date = datetime.datetime.now()
        
# class Document(db.Model):
#     """Document Table """
#     __tablename__ = "tb_documents"
#     document_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     document_name = db.Column(db.String(100), nullable=False)
#     config_seq_id = db.Column(db.Integer, nullable=True)
#     score = db.Column(db.Integer, nullable=True)
#     status = db.Column(db.String(1), nullable=False, default=STATUS["ACTIVE"])
#     created_date = db.Column(db.DateTime, nullable=True)
#     updated_date = db.Column(db.DateTime, nullable=True)

#     def __init__(self,document_name,config_seq_id,score):
#         self.document_name = document_name
#         self.config_seq_id = config_seq_id
#         self.score = score
#         self.created_date = datetime.datetime.now()


class Config(db.Model):
    """Config Table"""
    __tablename__ = "tb_config"
    seq_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_type = db.Column(db.String(1000), nullable=False)
    id_version = db.Column(db.Integer, nullable=False)
    config_id = db.Column(db.Integer, nullable=False)
    params_type = db.Column(db.String(50), nullable=False)
    params = db.Column(db.String(5000), nullable=False)
    params_dist = db.Column(db.Float, nullable=False, default=0.0)
    params_ratio = db.Column(db.Float, nullable=False, default=0.0)
    image_breath = db.Column(db.Float, nullable=False, default=0.0)
    image_length = db.Column(db.Float, nullable=False, default=0.0)
    image_key = db.Column(db.String(1000), nullable=False)
    status = db.Column(db.String(1), nullable=False, default=STATUS["ACTIVE"])
    created_date = db.Column(db.DateTime, nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,id_type,id_version,config_id,params_type,params,params_dist,params_ratio,image_breath,image_length,image_key):
        self.id_type = id_type
        self.id_version = id_version
        self.config_id = config_id
        self.params_type = params_type
        self.params = params
        self.params_dist = params_dist
        self.params_ratio = params_ratio
        self.image_breath = image_breath
        self.image_length = image_length
        self.image_key = image_key
        self.created_date = datetime.datetime.now()