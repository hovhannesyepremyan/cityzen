from django.contrib import admin
from .models import District


class DistrictAdmin(admin.ModelAdmin):
    pass


admin.site.register(District, DistrictAdmin)
