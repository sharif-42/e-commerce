from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from product.models import (
    Product,
    ProductBrand,
    ProductType,
    ProductGroup,
    ProductColor
)


@registry.register_document
class ProductDocument(Document):
    pk = fields.IntegerField()
    product_group = fields.ObjectField(properties={
        'name': fields.TextField(),
        'description': fields.TextField(),
        'is_available': fields.BooleanField(),
    })
    product_type = fields.ObjectField(properties={
        'name': fields.TextField(),
        'description': fields.TextField(),
        'is_available': fields.BooleanField(),
    })
    brand = fields.ObjectField(properties={
        'name': fields.TextField(),
        'description': fields.TextField(),
        'is_available': fields.BooleanField(),
    })
    unit = fields.IntegerField()
    uuid = fields.TextField()

    class Index:
        # Name of the Elasticsearch index
        name = 'products'
        # See Elasticsearch Indices API reference for available settings
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Product
        queryset_pagination = 2000

        fields = [
            'name',
            'short_description',
            'long_description',
            'pre_order',
            'is_available',
            'is_serviceable',
            'image_thumbnail',
            'image_alternative_1',
            'image_alternative_2',
            'image_alternative_3',
            'image_alternative_4',
            'valid_from',
            'valid_until',

        ]
        related_models = [
            ProductType,
            ProductGroup,
            ProductBrand,
        ]
        rebuild_from_value_list = True

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Product instance(s) from the related model.
                The related_models option should be used with caution because it can lead in the index
                to the updating of a lot of items.
                """
        if isinstance(related_instance, ProductType):
            return related_instance.products.all()
        if isinstance(related_instance, ProductBrand):
            return related_instance.products.all()
        if isinstance(related_instance, ProductBrand):
            return related_instance.products.all()
