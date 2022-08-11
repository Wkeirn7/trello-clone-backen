from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

# Create your views here.
class CreateNewUser(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            User.objects.create_user(username=username, password=password)