from rest_framework import serializers

from product.models import Product


class ProductOutPutSerializer(serializers.ModelSerializer):
    product_group = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    product_type = serializers.SerializerMethodField()
    image_thumbnail = serializers.SerializerMethodField()
    image_alternative_1 = serializers.SerializerMethodField()
    image_alternative_2 = serializers.SerializerMethodField()
    image_alternative_3 = serializers.SerializerMethodField()
    image_alternative_4 = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "uuid",
            "name",
            "brand",
            "product_group",
            "product_type",
            "short_description",
            "pre_order",
            "image_thumbnail",
            "image_alternative_1",
            "image_alternative_2",
            "image_alternative_3",
            "image_alternative_4",
        ]

    def get_product_group(self, instance):
        return instance.product_group.name if instance.product_group else None

    def get_brand(self, instance):
        return instance.brand.name if instance.brand else None

    def get_product_type(self, instance):
        return instance.product_type.name if instance.product_type else None

    def get_image_thumbnail(self, instance):
        return instance.image_thumbnail.url if instance.image_thumbnail else None

    def get_image_alternative_1(self, instance):
        return instance.image_alternative_1.url if instance.image_alternative_1 else None

    def get_image_alternative_2(self, instance):
        return instance.image_alternative_2.url if instance.image_alternative_2 else None

    def get_image_alternative_3(self, instance):
        return instance.image_alternative_3.url if instance.image_alternative_3 else None

    def get_image_alternative_4(self, instance):
        return instance.image_alternative_4.url if instance.image_alternative_4 else None
