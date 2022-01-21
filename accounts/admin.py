from django.contrib import admin

# Register your models here.

from .models import UserPersonalDetails,Address

admin.site.register(UserPersonalDetails)
admin.site.register(Address)
