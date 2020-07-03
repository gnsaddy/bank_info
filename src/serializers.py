from rest_framework import serializers
from .models import Bank, Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = (
            'ifsc', 'branch', 'bank', 'address',
            'city', 'district', 'state')
