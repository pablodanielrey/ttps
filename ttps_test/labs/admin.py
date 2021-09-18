from django.contrib import admin

# Register your models here.

from .models import LabResult, LabQuote, LabStatus, LabType, Lab, SocialSecurityInvoice, Extraction

admin.site.register(Lab)
admin.site.register(LabResult)
admin.site.register(LabQuote)
admin.site.register(LabStatus)
admin.site.register(LabType)
admin.site.register(SocialSecurityInvoice)
admin.site.register(Extraction)