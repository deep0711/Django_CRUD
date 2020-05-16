from django.contrib import admin

# Register your models here.

from .models import CRUDModel

admin.site.register(CRUDModel)