from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
# from django.db import connection

class APIResponseWrapperMiddleware(MiddlewareMixin):
    def should_not_process(self, response):
        return not isinstance(response, Response) \
            or response.data is None              \
            or "error" in response.data

    def process_response(self, request, response):
        # for q in connection.queries:
        #     print(q.get("sql", ""))

        if self.should_not_process(response):
            return response

        response.data = {
            "status": response.status_code,
            "data": response.data,
        }
        response._is_rendered = False 
        response.render()

        return response
