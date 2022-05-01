from rest_framework import serializers
from .models import CreditOffersModel


class CreditOffersSerializer(serializers.ModelSerializer):
    payment = serializers.IntegerField(default=None)
    class Meta:
        model = CreditOffersModel
        fields = '__all__'
