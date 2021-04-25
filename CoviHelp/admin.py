from django.contrib import admin

from .models import User, Hospital, Oxygen, Pharma
# Register your models here.

admin.site.register(User)
admin.site.register(Oxygen)
admin.site.register(Hospital)
admin.site.register(Pharma)
