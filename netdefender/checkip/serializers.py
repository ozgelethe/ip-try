from rest_framework import serializers
from .models import IPAddress

class IPAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPAddress
        fields = ['address', 'otx_info']
