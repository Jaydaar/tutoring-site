from django.contrib import admin

# Register your models here.
from tutor.models import Tutor

class TutorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tutor, TutorAdmin)