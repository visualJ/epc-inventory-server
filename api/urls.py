from django.conf.urls import url, include
from rest_framework import routers

from api.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
