from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from .serializer import ProductOutPutSerializer


class ProductSearchAPIView(APIView):
    # service_class = ''
    serializer_class = ProductOutPutSerializer
    # queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        products = Product.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
