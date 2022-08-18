from cgitb import lookup
from django.urls import path, include
from rest_framework import routers
from .views import UserBoardsViewSet, ListViewSet, CardViewSet, BoardPersonViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()

#URL Patterns:
#   boards/boards_list/
#   boards/boards_list/{board_pk}
#   boards/boards_list/{board_pk}/lists/
#   boards/boards_list/{board_pk}/lists/{list_pk}
#   boards/boards_list/{board_pk}/lists/{list_pk}/cards/
#   boards/boards_list/{board_pk}/lists/{list_pk}/cards/{card_pk}/

router.register(r'boards_list', UserBoardsViewSet, basename='boards_list')

boards_router = routers.NestedSimpleRouter(router, r'boards_list', lookup='boards_list')
boards_router.register(r'lists', ListViewSet, basename='lists')
boards_router.register(r'participants', BoardPersonViewSet, basename='participants')

list_router = routers.NestedSimpleRouter(boards_router, r'lists', lookup='lists')
list_router.register(r'cards', CardViewSet, basename='cards')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(boards_router.urls)),
    path(r'', include(list_router.urls)),
]