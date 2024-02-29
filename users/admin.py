from django.contrib import admin
from users.models import Profile,SMSCode


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'bio', 'age',)
    fields = ('user', 'bio', 'avatar', 'age')

admin.site.register(SMSCode)
