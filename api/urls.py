from django.conf.urls import url, include
from rest_framework import routers

from api.views import ProductViewSet, UpdateProductsView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^updateProducts', UpdateProductsView.as_view(), name="updateproductsview")
]
