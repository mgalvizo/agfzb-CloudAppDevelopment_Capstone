from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class

class CarModelAdmin(admin.ModelAdmin):
    fields = ['name', 'dealer_id', 'model_type', 'year']

# CarMakeAdmin class with CarModelInline

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

# Register models here

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)