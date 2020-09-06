from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """returns a list of APIView feature"""
        an_apiview = [
            'abc',
            'def',
            'efgh',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
