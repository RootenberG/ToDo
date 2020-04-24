from rest_framework import routers
from todolist.viewsets import ArticleViewSet
router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
