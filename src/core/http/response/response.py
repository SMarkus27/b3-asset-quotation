from flask import Response, jsonify, make_response

from src.core.http.codes import HttpCodes


def response(data: dict | None = None, http_code: HttpCodes = HttpCodes.OK, message: str | None = None) -> Response:
    status = http_code.value[0]

    return make_response(
        jsonify(
            code=http_code.name,
            status=status,
            message=message or http_code.value[1],
            data=data if data else {},
        ),
        status,
    )