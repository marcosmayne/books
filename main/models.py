from django.db import models


class Author(models.Model):

    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):

    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):

    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):

    STATUS = (
        ('A', 'Available'),
        ('B', 'Borrowed'),
        ('D', 'Donation'),
        ('RE', 'Read'),
        ('RG', 'Reading'),
        ('NR', 'Not Read'),
    )
    
    class Meta:
        verbose_name = 'Book'
        ordering = ["title"]

    title = models.CharField(blank=False, null=False, max_length=100)
    sub_title =  models.CharField(blank=True, null=False, max_length=200)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.CharField(blank=False, null=False, max_length=100, default= "A", choices=STATUS)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return self.title
