from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = "news_mtm"
        ordering = ("name", )
        verbose_name = "category"
        verbose_name_plural = "categories"

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateField()
    categories = models.ManyToManyField(to=Category, blank=True, verbose_name="Категории")

    class Meta:
        app_label = "news_mtm"
        ordering = ("-publication_date", "title")
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


