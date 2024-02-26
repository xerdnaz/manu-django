from django.contrib import admin
from .models import Client, Beneficiary, Product, Riders, InsurancePlan

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "middle_name",)
    search_fields = ("id", "last_name", "first_name", "middle_name",)

@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "last_name", "first_name", "middle_name",)
    search_fields = ("id", "client__last_name",  "client__first_name", "client__middle_name", "last_name", "first_name", "middle_name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_type",)
    search_fields = ("id", "product_type",)

@admin.register(Riders)
class RidersAdmin(admin.ModelAdmin):
    list_display = ("id", "rider_type",)
    search_fields = ("id", "rider_type",)


@admin.register(InsurancePlan)
class InsurancePlanAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "policy_number", "product",)
    search_fields = ("id", "client__last_name",  "client__first_name", "client__middle_name", "policy_number", "product__product_type",)