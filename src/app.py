
from apiflask import APIFlask
from decouple import config

from src.controller import api_v1_blueprint
from src.core.config.extensions import db
from src.core.config.settings import config_
from src.models.entities.assets_quotation import AssetsQuotation

def create_app(config_name: str):
    app = APIFlask(__name__)

    app.config.from_object(config_[config_name])
    app.register_blueprint(api_v1_blueprint)

    db.init_app(app)

    with (app.app_context()):
        db.create_all()

    return app


if __name__ == '__main__':
    config_name = config('FLASK_CONFIG', 'development')
    create_app(config_name).run(debug=True)
