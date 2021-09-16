from django.contrib import admin

# Register your models here.

from .models import Person, IdentificationType, Identification

admin.site.register(Person)
admin.site.register(Identification)
admin.site.register(IdentificationType)