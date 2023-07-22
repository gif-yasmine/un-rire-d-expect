from django.db import models
from django.contrib.auth.models import AbstractUser

#  Create your models here.

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_related_groups',
        blank=True,
        verbose_name='user groups'
    )

    # Résolution du conflit pour le champ "user_permissions"
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_related_permissions',
        blank=True,
        verbose_name='user permissions'
    )

    is_admin = models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)