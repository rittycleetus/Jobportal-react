from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Job Seeker'),
        (2, 'Employer'),
    )
    user_type = models.IntegerField(default=1, choices=USER_TYPE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return self.username

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

class Job(models.Model):
    employer_profile = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, null=True)
    designation = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)
    last_date = models.DateField()
    posting_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    location = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=20, choices=[('Full time', 'Full Time'), ('Part time', 'Part Time')], null=True, blank=True)

class Notification(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    action = models.CharField(max_length=50, null=True)
    notification_type = models.CharField(max_length=50, null=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def mark_as_unread(self):
        self.is_read = False
        self.save()

class JobApplication(models.Model):
    jobseeker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    selected = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

@receiver(models.signals.post_save, sender=JobApplication)
def create_notification(sender, instance, **kwargs):
    existing_notification = Notification.objects.filter(
        email=instance.jobseeker.email,
        action='Applied for a job',
        notification_type='application',
        is_read=False
    ).first()

    if not existing_notification:
        Notification.objects.create(
            name=instance.jobseeker.username,
            email=instance.jobseeker.email,
            action='Applied for a job',
            notification_type='application'
        )

class EmployerNotification(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE,null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE,null=True)
    application_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(
        max_length=50,
        choices=[('applied', 'Applied Job'), ('selected', 'Selected Job')],
        null=True
    )

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.save()


class VerifiedUser(models.Model):
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50) 

    def __str__(self):
        return self.name

class RejectedJob(models.Model):
    job_seeker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    rejection_date = models.DateTimeField(auto_now_add=True)


class Notification1(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class Verification(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - Verified: {self.is_verified}'

class TempJobSeekerProfile(models.Model):
    name = models.CharField(_('name'), max_length=255)
    dob = models.DateField(_('date of birth'))
    username = models.CharField(_('username'), max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(_('profile picture'), upload_to='temp_profile_pictures/', blank=True, null=True)
    educational_info = models.TextField(_('educational information'), blank=True, null=True)
    address = models.TextField(_('address'), blank=True, null=True)
    email = models.EmailField(_('email'), unique=True)  
    password = models.CharField(_('password'), max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class JobSeeker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_approved = models.BooleanField(default=False)  

    def __str__(self):
        return self.name
        
class TempEmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='employer_logos/')
    website = models.URLField()
    address = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=128, blank=True, null=True)  
    blocked = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Employer1(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_approved = models.BooleanField(default=False)  

    def __str__(self):
        return self.name