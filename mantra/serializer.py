from rest_framework import serializers
from .models import Mantra


class MantraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantra
        fields = '__all__'