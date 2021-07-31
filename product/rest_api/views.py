from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from product.rest_api.serializers.product_serializer import ProductOutPutSerializer
from product.services.product_service import ProductService


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductOutPutSerializer
    service_class = ProductService

    def list(self, request, *args, **kwargs):
        products = self.service_class().get_products()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
