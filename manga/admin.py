from django.contrib import admin
from . import models

admin.site.register(models.Manga)
admin.site.register(models.Reviews)
admin.site.register(models.Genre)
