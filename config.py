import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        "postgres://mqoqrgevidbckm:3493a12831192165d630b545b22a6d9bcb3b34da85b99f7ac8b5f103fbc098ff@ec2-52-86-116-94.compute-1.amazonaws.com:5432/danqhipjt3o754"
    DEBUG = True
