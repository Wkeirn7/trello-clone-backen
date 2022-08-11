from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),
    path('user_accounts/', include('user_accounts.urls')),
]
