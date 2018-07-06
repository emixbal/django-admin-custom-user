from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Unit(models.Model):
    class Meta:
        # app_label = 'client'
        db_table = 'unit'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, default="")

    # general
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='unit_created_by'
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='unit_updated_by'
    )
