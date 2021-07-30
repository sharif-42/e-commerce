from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from .serializer import ProductOutPutSerializer
from ..services.product_search_service import ProductSearchService


class ProductSearchAPIView(ListAPIView):
    service_class = ProductSearchService
    serializer_class = ProductOutPutSerializer
    # queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        query_params_dict = self.request.query_params.dict()

        queryset = self.service_class().get_products(query_params=query_params_dict)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
