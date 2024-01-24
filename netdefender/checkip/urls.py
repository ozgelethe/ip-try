from django.urls import path
from .views import IPAddressListCreateView

urlpatterns = [
    path('ip-addresses/', IPAddressListCreateView.as_view(), name='ip-address-list-create'),
]