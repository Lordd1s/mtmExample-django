from django.contrib import admin
from news_mtm import models

# Register your models here.
admin.site.register(models.News)
admin.site.register(models.Category)