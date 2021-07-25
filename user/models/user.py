import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, password, email=None, contact_number='', location=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('User must have an username')
        if location == 'super':
            username = username
        user = self.model(username=username, email=email, phone_number=contact_number)
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
            location='super'
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_dashboard_user = True
        user.is_pending = False
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("UUID"),
        help_text=_("This will be exposed to the outside world."),
    )
    username = models.CharField(
        verbose_name='Username',
        unique=True,
        max_length=255,
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("User first name")
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("User last/nick name")
    )
    mid_name = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("User middle name")
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=64,
        verbose_name='Contact Number',
        blank=True,
        help_text=_('User Contact Number')
    )
    # user boolean field
    is_active = models.BooleanField(default=True, help_text=_('Inactive user can do nothing in the system.'))
    is_pending = models.BooleanField(default=True, help_text=_('User activity is pending for some reasons.'))
    is_admin = models.BooleanField(default=False, help_text=_('User is a admin user.'))
    is_dashboard_user = models.BooleanField(default=False, help_text=_('User is a dashboard user.'))

    # blocking related fields
    is_blocked = models.BooleanField(default=False, help_text=_('User is blocked by authority for some reasons.'))

    # common fields
    join_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('-id',)
        # TODO: Define index

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
