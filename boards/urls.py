from django.urls import path
from rest_framework import routers
from .views import UserBoardsViewSet, ListViewSet, CardViewSet

router = routers.SimpleRouter()

router.register(r'boards_list', UserBoardsViewSet)
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = router.urls
