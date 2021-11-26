import datetime
import json, requests
from sqlalchemy import and_

from app import app,  db, STATUS

# Model Class

class Config(db.Model):
    """Config Table"""
    __tablename__ = "tb_config"
    seq_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_type = db.Column(db.Integer, nullable=False)
    id_params = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(1), nullable=False, default=STATUS["ACTIVE"])
    created_date = db.Column(db.DateTime, nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,id_type,id_params):
        self.id_type = id_type
        self.id_params = id_params
        self.created_date = datetime.datetime.now()
        
class Document(db.Model):
    """Document Table """
    __tablename__ = "tb_documents"
    document_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document_name = db.Column(db.String(100), nullable=False)
    config_seq_id = db.Column(db.Integer, nullable=True)
    score = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(1), nullable=False, default=STATUS["ACTIVE"])
    created_date = db.Column(db.DateTime, nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self,document_name,config_seq_id,score):
        self.document_name = document_name
        self.config_seq_id = config_seq_id
        self.score = score
        self.created_date = datetime.datetime.now()