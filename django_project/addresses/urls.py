from django.urls import path

from .views import (
    AddressListView,
    AddressDetailView,
    AddressUpdateView,
    AddressDeleteView,
)

urlpatterns = [
    path("", AddressListView.as_view(), name="address-list"),
    path("<int:pk>", AddressDetailView.as_view(), name="address-detail"),
    path("<int:pk>/edit", AddressUpdateView.as_view(), name="address-update"),
    path("<int:pk>/delete", AddressDeleteView.as_view(), name="address-delete"),
]
