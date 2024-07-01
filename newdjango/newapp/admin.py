from django.contrib import admin
from .models import JobSeekerProfile, CustomUser, EmployerProfile, TempJobSeekerProfile,Notification

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

@admin.register(TempJobSeekerProfile)
class TempJobSeekerProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'username', 'email', 'created_at', 'is_approved']
    list_filter = ['created_at', 'is_approved']
    actions = ['approve_selected', 'reject_selected']

    def approve_selected(self, request, queryset):
        for temp_profile in queryset:
            # Optionally, move data to JobSeekerProfile model and delete temp profile
            temp_profile.delete()  # Delete temporary profile after approval
            # Create notification for admin or other actions
            Notification.objects.create(
                name=temp_profile.name,
                email=temp_profile.email,
                action='Job seeker approved',
                notification_type='approval'
            )
        self.message_user(request, "Selected profiles approved successfully.")

    def reject_selected(self, request, queryset):
        for temp_profile in queryset:
            temp_profile.delete()  # Delete temporary profile after rejection
            # Create notification for admin or other actions
            Notification.objects.create(
                name=temp_profile.name,
                email=temp_profile.email,
                action='Job seeker rejected',
                notification_type='rejection'
            )
        self.message_user(request, "Selected profiles rejected successfully.")
