from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from common.constants import ColorOptions


class ProductColor(BaseModel):
    color_name = models.CharField(
        max_length=128,
        help_text=_("Color Name."),
        verbose_name='Color Name'
    )
    color_code = models.CharField(
        max_length=128,
        help_text=_("Color Code."),
        unique=True,
        choices=ColorOptions.CHOICES,
        verbose_name='Color Code'
    )
    is_available = models.BooleanField(
        default=True,
        help_text=_("color is available or not")
    )

    class Meta:
        ordering = ['-id', 'color_code']
        indexes = [
            models.Index(
                fields=['color_code', 'is_available', ]
            ),
        ]

    def __str__(self):
        return self.color_code
