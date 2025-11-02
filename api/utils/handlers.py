from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # TODO: improve error messages
    if response is not None and response.data is not None:
        key = next(iter(response.data))
        response.data = {
            "status": response.status_code,
            "error": {
                "message": repr(response.data.get(key)),
                "code": exc.__class__.__name__,
            },
        }
        return response

    response = Response(
        {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "error": {
                "message": str(exc),
                "code": "InternalServerError",
            },
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

    return response
