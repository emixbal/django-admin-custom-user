from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Unit

class UnitSerializer(serializers.ModelSerializer):
    created_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)
    updated_by = RecursiveField('user.serializers.UserSerializerSimple', read_only=True)

    class Meta:
        model = Unit
        fields = (
            'id',
            'code',
            'name',
            'description',

            # general
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )

# exclude relationship to avoid recursive load
class UnitSerializerSimple(UnitSerializer):
    class Meta:
        model = Unit
        fields = (
            'id',
            'code',
            'name',
            'description',

            # general
            'is_active',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )
