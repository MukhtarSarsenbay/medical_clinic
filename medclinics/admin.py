from django.contrib import admin
from .models import Appeal, Service, Diagnosis

admin.site.register(Appeal)
admin.site.register(Service)
admin.site.register(Diagnosis)