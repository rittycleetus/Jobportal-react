from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Job Seeker'),
        (2, 'Employer'),
    )
    user_type = models.IntegerField(default=1, choices=USER_TYPE_CHOICES)

    # Add unique related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups'  # Unique related_name for CustomUser groups
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'  # Unique related_name for CustomUser user_permissions
    )

    def __str__(self):
        return self.username  # Or any other meaningful representation

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(_('name'), max_length=255)
    dob = models.DateField(_('date of birth'))
    username = models.CharField(_('username'), max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(_('profile picture'), upload_to='profile_pictures/', blank=True, null=True)
    educational_info = models.TextField(_('educational information'), blank=True, null=True)
    address = models.TextField(_('address'), blank=True, null=True)

    class Meta:
        verbose_name = _('job seeker profile')
        verbose_name_plural = _('job seeker profiles')

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(_('company name'), max_length=255)
    username = models.CharField(_('username'), max_length=50, unique=True, blank=True, null=True)
    logo = models.ImageField(_('logo'), upload_to='employer_logos/')
    website = models.URLField(_('website URL'))
    address = models.TextField(_('address'))

    class Meta:
        verbose_name = _('employer profile')
        verbose_name_plural = _('employer profiles')
