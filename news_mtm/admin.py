from django.contrib import admin
from news_mtm import models

# Register your models here.
admin.site.register(models.Category)


class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ["categories"]


admin.site.register(models.News, CategoryAdmin)