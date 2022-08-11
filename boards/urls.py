from django.urls import path
from rest_framework import routers
from .views import UserBoardsViewSet, ListViewSet, CardViewSet

router = routers.SimpleRouter()

router.register(r'boards_list', UserBoardsViewSet, basename='boards_list')
router.register(r'lists', ListViewSet, basename='lists')
router.register(r'cards', CardViewSet, basename='cards')

urlpatterns = router.urls
