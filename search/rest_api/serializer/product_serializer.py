from rest_framework import serializers

from product.models import Product


class ProductOutPutSerializer(serializers.ModelSerializer):
    product_group = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    product_type = serializers.SerializerMethodField()
    image_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "uuid",
            "name",
            "unit",
            "brand",
            "product_group",
            "product_type",
            "short_description",
            "long_description",
            "weight",
            "release_date",
            "pre_order",
            "is_serviceable",
            "image_thumbnail",

        ]

    def get_product_group(self, instance):
        return instance.product_group.name if instance.product_group else None

    def get_brand(self, instance):
        return instance.brand.name if instance.brand else None

    def get_product_type(self, instance):
        return instance.product_type.name if instance.product_type else None

    def get_image_thumbnail(self, instance):
        return instance.image_thumbnail.url if instance.image_thumbnail else None
