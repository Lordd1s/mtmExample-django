from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = "news_mtm"
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(to=Category, blank=True, verbose_name="Категории")

    class Meta:
        app_label = "news_mtm"
        ordering = ("-publication_date", "title")
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
