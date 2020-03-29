from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APi View"""

    def get(self, request):
        """Returns a list of APIView features"""
        an_apiview = ["Hoooooooooooooooooooooooooooooooooooola"]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
