# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db


class AppAccessLog(db.Model):
    __tablename__ = 'app_access_log'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.BigInteger, nullable=False, index=True, server_default=db.FetchedValue())
    referer_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    target_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    query_params = db.Column(db.Text, nullable=False)
    ua = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    ip = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    note = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AppErrorLog(db.Model):
    __tablename__ = 'app_error_log'

    id = db.Column(db.Integer, primary_key=True)
    referer_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    target_url = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    query_params = db.Column(db.Text, nullable=False)
    content = db.Column(db.String, nullable=False)
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.BigInteger, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    mobile = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    email = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    avatar = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    login_name = db.Column(db.String(20), nullable=False, unique=True, server_default=db.FetchedValue())
    login_pwd = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    login_salt = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
