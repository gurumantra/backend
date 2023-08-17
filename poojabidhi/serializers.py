from rest_framework import serializers
from .models import PoojaBidhi


class PoojaBidhiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoojaBidhi
        fields = '__all__'