from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializer.user_serializer import UserSerializer
from user.models import User


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ''
    permission_classes = ''

