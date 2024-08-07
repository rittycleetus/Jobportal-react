

from django.contrib import admin
from .models import JobSeekerProfile, CustomUser, EmployerProfile, TempJobSeekerProfile, JobSeeker,TempEmployerProfile,Employer1

admin.site.register(JobSeekerProfile)
admin.site.register(EmployerProfile)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')
    list_filter = ('user_type',)
    search_fields = ('username', 'email',)
    fieldsets = (
        (None, {'fields': ('username', 'email')}),
        ('Permissions', {'fields': ('user_type',)}),
    )

admin.site.register(JobSeeker)
admin.site.register(TempJobSeekerProfile)

admin.site.register(Employer1)
admin.site.register(TempEmployerProfile)
