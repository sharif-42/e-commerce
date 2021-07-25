from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class ProductType(BaseModel):
    name = models.CharField(
        max_length=128,
        help_text=_("Name of the Option Group"),
        unique=True
    )
    description = models.TextField(
        help_text=_("Description of the Option Group")
    )
    is_available = models.BooleanField(
        default=True,
        help_text=_("Brand is available or not")
    )

    class Meta:
        ordering = ['-id', 'name']
        indexes = [
            models.Index(
                fields=['name', 'is_available', ]
            ),
        ]

    def __str__(self):
        return self.name
