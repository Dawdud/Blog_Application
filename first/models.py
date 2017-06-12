# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify
import uuid
class TypeOfDocument(models.Model):
     nameofdocument= models.CharField(max_length=128, unique=True)

     class Meta:
         verbose_name_plural = "TypeOfDocument"
         def __str__(self):
            return self.name

class Category(models.Model):
        name= models.CharField(max_length=128, unique=True)
        slug= models.SlugField(blank=True, unique=True, default=uuid.uuid1 )
        def save(self,*args,**kwargs):
            self.slug= slugify(self.name)
            super(Category, self).save(*args,**kwargs)

        class Meta:
            verbose_name_plural = "Categories"

        def __str__(self):
                return self.name



class Books(models.Model):
    category= models.ForeignKey(Category)
    Title= models.CharField(max_length=128)
    OriginalTitle= models.CharField(max_length=128)
    Author= models.CharField(max_length=128)
    entry= models.CharField(max_length=128, blank=True)
    Tag= models.CharField(max_length=128, blank=True)
    Publisher= models.CharField(max_length=128)
    ISBN= models.BigIntegerField(null=True)
    UKD= models.CharField(max_length=128, blank=True)
    DatePublished= models.DateField(auto_now=False, null=True)
    BookImage= models.ImageField(upload_to='Books', blank=True)
    url= models.URLField(blank=True)
    slugbook= models.SlugField(blank= True, unique=True,default=uuid.uuid1)
    id = models.AutoField(primary_key=True, default=10, )

    def save(self, *args,**kwargs):
        self.slugbook= slugify(self.Title)
        super(Books, self).save(*args,**kwargs)
    class Meta:
        verbose_name_plural="Books"
    def __str__(self):
            return self.Title



