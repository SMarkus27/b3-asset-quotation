from apiflask import APIBlueprint

from src.controller.quotation.controller import asset_quotation_bp

api_v1_blueprint = APIBlueprint('v1', __name__, url_prefix='/v1')

api_v1_blueprint.register_blueprint(asset_quotation_bp)