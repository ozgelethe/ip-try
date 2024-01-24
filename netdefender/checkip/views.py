from rest_framework import generics
from .models import IPAddress
from .serializers import IPAddressSerializer
import requests

class IPAddressListCreateView(generics.ListCreateAPIView):
    
    # pylint: disable=E1101
    queryset = IPAddress.objects.all()
    serializer_class = IPAddressSerializer
    template_name = 'checkip/ipaddress_list.html'  # Add this line

    def perform_create(self, serializer):
        ip_address = serializer.validated_data['address']
        otx_api_key = '10b3c85ec7bc3e838a597def76837b7d0dc4b1f770b75a849ade86970aa4edd5'  # Replace with your OTX API key

        # Make request to OTX API
        otx_url = f'https://otx.alienvault.com/api/v1/indicators/IPv4/{ip_address}/'
        headers = {'X-OTX-API-KEY': otx_api_key}
        response = requests.get(otx_url, headers=headers)

        if response.status_code == 200:
            otx_data = response.json()
            serializer.save(otx_info=otx_data)
        else:
            serializer.save()  # Save the IP address even if the OTX request fails
