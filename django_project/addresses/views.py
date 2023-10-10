from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Address


class AddressListView(ListView):
    model = Address


class AddressDetailView(DetailView):
    model = Address


class AddressUpdateView(UpdateView):
    model = Address


class AddressDeleteView(DeleteView):
    model = Address
