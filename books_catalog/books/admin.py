from django.contrib import admin

from books import models

admin.site.register(models.Book)
admin.site.register(models.Author)
