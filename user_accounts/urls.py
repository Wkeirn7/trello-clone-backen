from django.urls import path
from .views import CreateNewUser
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('create_account/', CreateNewUser.as_view(), name='create_account'),
    path('get_token/', obtain_auth_token, name='get_token'),
]
