from rest_framework import serializers
from .models import ChadParba


class ChadParbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChadParba
        fields = '__all__'
    