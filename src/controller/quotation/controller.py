from apiflask import APIBlueprint
from flask import Response

from src.core.http.response.response import response
from src.services.quotation.service import QuotationService

asset_quotation_bp = APIBlueprint('asset_quotation_bp', __name__, url_prefix='/asset-quotation')


@asset_quotation_bp.get("/")
def update_asset_quotation() -> Response:
    data = QuotationService.save()
    return response(data={"result": data})

