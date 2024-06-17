from django.contrib import admin

from .models import Career

# Register your models here.
class CareerAdmin(admin.ModelAdmin):
    list_display = ('specialization','interest','skills','certification','recommended_role')  
    # search_fields = ['olympiad_name']  
admin.site.register(Career, CareerAdmin)
