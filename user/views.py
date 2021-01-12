from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer
from .models import UserModel
from rest_framework.views import APIView
from rest_framework.response import Response


class SingUpView(CreateAPIView):
    serializer_class = UserSerializer


class UserView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAdminUser]


class GetUserDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status.HTTP_200_OK)
