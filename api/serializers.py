from rest_framework import serializers
from .models import Banks, Branches


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ['id', 'name']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['bank_id', 'ifsc', 'branch', 'address', 'city', 'state', 'district']
