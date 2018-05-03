from django.db import models
from django.utils.translation import ugettext_lazy as _
from allauth.app_settings import USER_MODEL

# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

SUBJECT_CHOICES = (
    ('01', 'Math'),
    ('02', 'English'),
    ('03', 'Physics'),
    ('04', 'Information Technology'),
)

LOCATION_CHOICES = (
    ('01', 'St. Joseph'),
    ('02', 'San Juan'),
)
class Tutor(models.Model):
    first_name = models.CharField(max_length=255, default='My', blank=True, null=True)
    last_name = models.CharField(max_length=255, default='My', blank=True, null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    subjects = models.CharField(max_length=255, choices=SUBJECT_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES, blank=True, null=True)
    # resume = models.OneToOneField('resume', on_delete=models.CASCADE)
    # is_verified = models.BooleanField()
    user = models.ForeignKey(USER_MODEL,
                             verbose_name=_('user'),
                             on_delete=models.CASCADE)
    # messages = models.ForeignKey('Messages', related_name='messages', on_delete=models.CASCADE)
    # rating_and_review = models.ForeignKey('ratings', related_name='ratings', on_delete=models.CASCADE)

    def add_subject(self):
        pass