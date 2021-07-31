from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from ..services.product_search_service import ProductSearchService
from product.rest_api.serializers.product_serializer import ProductOutPutSerializer


class ProductSearchAPIView(ListAPIView):
    service_class = ProductSearchService
    serializer_class = ProductOutPutSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20

    def get(self, request, *args, **kwargs):
        query_params_dict = self.request.query_params.dict()

        queryset = self.service_class().get_products(query_params=query_params_dict)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
