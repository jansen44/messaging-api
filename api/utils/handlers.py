from rest_framework.views import exception_handler
from rest_framework import status
import uuid

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.data is not None:
        response.data = {
            "status": response.status_code,
            "error": {
                "message": response.data.get("detail", "An error occurred."),
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
