from django.contrib import admin
from searchapp.models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(Restaurant, RestaurantAdmin)
