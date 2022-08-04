from django.urls import path
from rest_framework import routers
from .views import UserBoardsViewSet

router = routers.SimpleRouter()
router.register(r'boards_list', UserBoardsViewSet)
urlpatterns = router.urls
