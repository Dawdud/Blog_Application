# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from first.models import Books, Category, TypeOfDocument


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name','Title')}
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(TypeOfDocument)
# Register your models here.
