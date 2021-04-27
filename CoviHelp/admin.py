from django.contrib import admin

from .models import UserInfo, Hospital, Oxygen, Pharma
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Oxygen)
admin.site.register(Hospital)
admin.site.register(Pharma)
