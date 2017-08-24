# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify
import uuid

def upload_location(instance,filename):
    return "%s/%s"%(instance.id, filename)
class Category(models.Model):
        name= models.CharField(max_length=128, unique=True)
        slug= models.SlugField(blank=True, unique=True, default=uuid.uuid1 )
        image= models.ImageField(upload_to=upload_location)
        height_field= models.IntegerField()
        width_field= models.IntegerField()
        def save(self,*args,**kwargs):
            self.slug= slugify(self.name)
            super(Category, self).save(*args,**kwargs)

        class Meta:
            verbose_name_plural = "Categories"

        def __str__(self):
                return self.name


class News(models.Model):
      Title= models.CharField(max_length=128)
      image = models.ImageField(upload_to=upload_location)
      text= models.TextField()
      DatePublished = models.DateField(auto_now=False, null=True)

      def __str__(self):
          return self.Title


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



