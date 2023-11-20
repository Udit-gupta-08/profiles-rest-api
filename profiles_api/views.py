from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """test API view"""

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_apiview = [
        'Use HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Give you the most control over your application logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})
