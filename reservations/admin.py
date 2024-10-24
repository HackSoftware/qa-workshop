from django.contrib import admin
from reservations.models import Property, Guest, Reservation


class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "number_of_beds")
    exclude = ("owner",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def save_model(self, request, obj, form, change,):
        obj.owner = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Property, PropertyAdmin)


class GuestAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")
    exclude = ("owner",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def save_model(self, request, obj, form, change,):
        obj.owner = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Guest, GuestAdmin)


class ReservationAdmin(admin.ModelAdmin):
    exclude = ("owner",)
    list_display = ("property", "start_date", "end_date", "status")
    filter_horizontal = ("guests",)
    list_filter = ("status",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def save_model(self, request, obj, form, change,):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Reservation, ReservationAdmin)
