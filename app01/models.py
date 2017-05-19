#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.∂∂∂


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    class Meta:
        verbose_name_plural=u"作者"
    def __str__(self):
        return "<%s %s>"%(self.first_name,self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=64,unique=True)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    class Meta:
        verbose_name_plural=u"出版社"
    def __str__(self):
        return "<%s>"%(self.name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    class Meta:
        verbose_name_plural=u"书籍"
    def __str__(self):
        return "<%s>"%(self.title)