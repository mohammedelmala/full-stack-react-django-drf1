from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ServerListViewSet

router = DefaultRouter()
router.register('server', ServerListViewSet)

urlpatterns = [
    # path('', router.urls)
]+router.urls