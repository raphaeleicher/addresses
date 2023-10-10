from django.contrib import admin
from .models import Address, Salutation, GivenName, LastName, Street

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Salutation)
class SalutationAdmin(admin.ModelAdmin):
    pass


@admin.register(GivenName)
class GivenNameAdmin(admin.ModelAdmin):
    pass

@admin.register(LastName)
class LastNameAdmin(admin.ModelAdmin):
    pass

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    pass

