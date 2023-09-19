from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', 'password')
    search_fields = ('email', 'name', 'phone', 'password')


admin.site.register(User, UserAdmin)