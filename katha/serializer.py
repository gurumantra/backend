from rest_framework import serializers
from .models import Katha


class KathaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Katha
        fields = '__all__'
        depth = 1

