from django.contrib import admin
from .models import JobSeekerProfile
from .models import CustomUser
# Register your models here.
admin.site.register(JobSeekerProfile)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')  # Customize displayed fields
    list_filter = ('user_type',)  # Add filters for user_type
    search_fields = ('username', 'email')  # Add search functionality

    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        ('Permissions', {'fields': ('user_type',)}),
    )