from rest_framework import viewsets
from rest_framework.response import Response

class TestDataViewSet(viewsets.ViewSet):
    def list(self, request):
        data = [
            {"id": 1, "name": "Item 1", "description": "Description for Item 1"},
            {"id": 2, "name": "Item 2", "description": "Description for Item 2"},
        ]
        return Response(data)
