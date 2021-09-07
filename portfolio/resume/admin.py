from django.contrib import admin
from resume.models import skill,experience,education,license
# Register your models here.
admin.site.register(skill)
admin.site.register(experience)
admin.site.register(education)
admin.site.register(license)
