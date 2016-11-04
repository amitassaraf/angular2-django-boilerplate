from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError

from {{cookiecutter.app_name}}.users.serializers import UserSerializer


class Login(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        form = AuthenticationForm(request, data=request.data)
        if not form.is_valid():
            raise ValidationError(form.errors)

        user = form.get_user()
        login(request, user)

        return Response(UserSerializer(user).data)


class Logout(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        logout(request)

        return Response({'status': 'success'})


class ActiveUser(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        return Response(UserSerializer(request.user).data)

