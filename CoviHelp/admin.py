from django.contrib import admin

from .models import UserInfo, Hospital, Oxygen, Pharma, Plasma, Report, Feedback
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Oxygen)
admin.site.register(Hospital)
admin.site.register(Pharma)
admin.site.register(Plasma)
admin.site.register(Report)
admin.site.register(Feedback)