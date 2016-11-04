from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from {{cookiecutter.app_name}}.users.models import User
from {{cookiecutter.app_name}}.users.permissions import IsOwnerOrReadOnly
from {{cookiecutter.app_name}}.users.serializers import UserSerializer


@ensure_csrf_cookie
def home(request):
    return render(request, 'index.html', {
        'USE_LIVE_RELOAD': False # settings.DEBUG
    })


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsOwnerOrReadOnly()]


