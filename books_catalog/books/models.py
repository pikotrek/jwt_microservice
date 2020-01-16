from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    authors = models.ManyToManyField(
        'Author',
        related_name='books'
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '%s (%s)' % (self.title, self.pages)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
