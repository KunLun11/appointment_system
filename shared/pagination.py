from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class DefaultPagination(LimitOffsetPagination):
    max_limit = None
    count_header_name: str = "x-count"

    def get_paginated_response(self, data):
        return Response({"data": data}, headers={self.count_header_name: self.count})

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "required": ["data"],
            "properties": {
                "data": schema,
            },
        }
