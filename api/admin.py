from django.contrib import admin

# Register your models here.
from .models import Banks,Branches

admin.site.register(Banks)
admin.site.register(Branches)
