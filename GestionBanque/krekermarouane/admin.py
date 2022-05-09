from django.contrib import admin
from .models import Client
from .models import Compte
from .models import Operation
# Register your models here.

admin.site.register(Client)
admin.site.register(Compte)
admin.site.register(Operation)