from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


class CommoResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthView(APIView):
    """
        User login
    """
    @swagger_auto_schema(
        request_body=LoginRequestSerializer,
        response={200: CommoResponseSerializer}
    )
    def post(self, request):
        return Response(CommoResponseSerializer({
            'status': 0,
            'message': 'Good'
        }).data)


@api_view()
def hello(request):
    return Response({"message": "hello"})
