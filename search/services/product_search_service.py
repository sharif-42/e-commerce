from django.utils import timezone
from elasticsearch_dsl import Q

from product.models import Product
from ..documents import ProductDocument


class ProductSearchService:
    document_class = ProductDocument

    def get_products(self, query_params):
        now = timezone.now()
        search_keyword = query_params.get("keyword")

        es_query = self.document_class.search().query(
            Q("match", is_available=True)
            & Q("range", valid_from={"lte": now})
            & Q("range", valid_until={"gte": now})
        )
        if search_keyword:
            es_query = es_query.query(
                Q("match", name=search_keyword)
            )
        return es_query.execute()


