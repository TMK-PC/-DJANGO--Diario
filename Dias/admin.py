from django.contrib import admin
from .models import Dias

# Register your models here.

class DiasAdmin(admin.ModelAdmin):
    list_display = ('data',)  
    search_fields = ('data', )

admin.site.register(Dias, DiasAdmin)