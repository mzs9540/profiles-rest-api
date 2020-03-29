from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test APi View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request):
        """Returns a list of APIView features"""
        an_apiview = ["Hoooooooooooooooooooooooooooooooooooola"]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create A hello meassage with ouur name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an Object"""
        return Response({'method':"PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELET'})
