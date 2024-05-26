from django.contrib import admin
from data.models import UserDeviceMetabolicData


class UserDeviceMetabolicDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserDeviceMetabolicData, UserDeviceMetabolicDataAdmin)