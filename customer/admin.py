from django.contrib import admin
from django.contrib import admin
from .models import customer
from .models import Questionaire
from .models import StatAdmin

admin.site.register(customer)
admin.site.register(Questionaire, StatAdmin)

# Register your models here.