# Create your views here.
import hashlib

import math
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Product, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductsView(APIView):
    def post(self, request):
        for product in request.data["products"]:
            if "header" in product and "domainManager" in product and "objectClass" in product and "serialNumber" in product and "location" in product:
                header = product["header"]
                domainManager = product["domainManager"]
                objectClass = product["objectClass"]
                serialNumber = product["serialNumber"]
                location = product["location"]
                filtered_products = Product.objects.filter(domainManager=domainManager, serialNumber=serialNumber, objectClass=objectClass)
                if not filtered_products:
                    new_id = int(hashlib.sha1("".join(map(str, [domainManager, objectClass, serialNumber])).encode()).hexdigest(), 16)
                    #short_id = int(new_id/math.pow(10, 32))
                    short_id = new_id % 2**31
                    print(short_id)
                    new_product = Product(id=short_id, header=header, domainManager=domainManager, serialNumber=serialNumber, objectClass=objectClass, location=location )
                    new_product.save()
                print(filtered_products)
        for product in Product.objects.all():
            for req_product in request.data["products"]:
                if product.domainManager == req_product["domainManager"] and product.objectClass == req_product["objectClass"] and product.serialNumber == req_product["serialNumber"]:
                    break
            else:
                product.delete()

        response_dict = {"Success": True}
        return Response(response_dict)
