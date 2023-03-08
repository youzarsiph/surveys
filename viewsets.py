""" ViewSets """


from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwner
from users.serializers import UserSerializer, UserCreationSerializer


# Create your viewsets here.
User = get_user_model()


class UserViewSet(ModelViewSet):
    """ User ViewSet """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_permissions(self):
        """ Return permissions """

        if self.action == 'create':
            self.permission_classes = []

        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        """ Return serializer  """

        if self.action == 'create':
            self.serializer_class = UserCreationSerializer

        return super().get_serializer_class()

    def perform_create(self, serializer):
        """ Encrypt the password """

        serializer.save(
            password=make_password(
                serializer.validated_data['password']
            )
        )
