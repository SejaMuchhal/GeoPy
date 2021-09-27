from django.urls import path
from .views import AddressDetails

urlpatterns = [
    path('getAddressDetails', AddressDetails.as_view(), name="get-address-detail"),
]
