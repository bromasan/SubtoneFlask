from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_cors import CORS, cross_origin

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)

login.login_view = 'login'


def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../client/build', static_url_path='/')
    app.config.from_object(config_class)
    CORS(app)
    migrate.init_app(app, db)
    db.init_app(app)


from app import routes, models

if __name__ == '__main__':
    app.run()
