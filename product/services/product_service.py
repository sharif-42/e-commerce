from ..models import Product


class ProductService:
    model = Product

    def get_products(self):
        products = self.model.objects.filter(
            is_available=True,
            unit__gte=1
        )
        return products
