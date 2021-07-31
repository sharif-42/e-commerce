from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from product.rest_api.serializers.product_serializer import ProductOutPutSerializer
from product.services.product_service import ProductService


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductOutPutSerializer
    service_class = ProductService
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20

    def list(self, request, *args, **kwargs):
        products = self.service_class().get_products()
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
