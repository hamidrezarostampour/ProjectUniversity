from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[1][1]['fields'] = ('fullname', 'address', 'email')
UserAdmin.list_display += ('fullname', )

admin.site.register(User, UserAdmin)