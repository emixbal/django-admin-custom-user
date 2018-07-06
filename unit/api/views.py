from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import filters, FilterSet
from django.db import models as django_models
from rest_framework.pagination import LimitOffsetPagination
from rest_framework_filters import backends
from rest_framework.decorators import action

from ..models import Unit
from ..serializers import UnitSerializer

class UnitFilter(FilterSet):
    createdAt_gte = django_filters.DateTimeFilter(name="createdAt", lookup_expr='gte')
    class Meta:
        model = Unit
        fields = ['code', 'name', 'createdAt_gte',]

class UnitViewset(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    pagination_class = LimitOffsetPagination

    filter_backends = (
        # backends.ComplexFilterBackend,
        SearchFilter,
        OrderingFilter,
    )
    filter_fields = ('code', 'name', 'description',)
    filter_class = UnitFilter
    # search_fields = ('code', 'name', 'description',)
    ordering_fields = ('__all__')

    # custom create with relation
    def create(self, request, format='json'):
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(created_by=request.user, updated_by=request.user)
            if instance:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_200_OK)

    # custom update with relation
    def partial_update(self, request, pk=None, format='json'):
        instance = self.queryset.get(pk=pk)
        serializer = UnitSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            unit = serializer.save(updated_by=request.user)
            if unit:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': serializer.errors}, status=status.HTTP_200_OK)

    @action(methods=['get'], permission_classes=[IsAuthenticated], detail=False)
    def get_schema(self, request):
        fields = Unit._meta.get_fields()
        field_names = [f.name for f in fields
            if not (f.is_relation)]

        return Response(
            field_names,
            status=status.HTTP_200_OK
        )
