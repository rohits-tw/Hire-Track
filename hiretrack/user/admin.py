from django.contrib import admin
from .models import CustomUser, UserDetail

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_active', 'is_staff')
    search_fields = ('username', 'email')


admin.site.register(UserDetail)