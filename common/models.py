import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models.user import User


class BaseModel(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("UUID"),
        help_text=_("This will be exposed to the outside world."),
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_('who created.'),
        related_name='creators'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_('who updated.'),
        blank=True, null=True,
        related_name='updators',
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class EmailTemplate(BaseModel):
    mail_type = models.CharField(
        verbose_name='Mail Type',
        unique=True,
        max_length=255,
        help_text=_("What type of mail.")
    )
    subject = models.CharField(
        verbose_name='Subject',
        unique=True,
        max_length=255,
        help_text=_("Subject of the mail.")
    )
    mail_text = models.TextField(
        verbose_name='Mail Text',
        help_text=_("Body of the mail.")
    )

    class Meta:
        ordering = ['-id']
        indexes = [
            models.Index(
                fields=['mail_type', 'subject', ]
            ),
        ]

    def __str__(self):
        return self.mail_type
