from rest_framework import serializers
from .models import Sotrudniki


class HoseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sotrudniki
        fields = ('fio', 'dol', 'uda', 'dat')
