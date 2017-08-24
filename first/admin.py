# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from first.models import Books, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name','Title')}
admin.site.register(Books)
admin.site.register(Category)
# Register your models here.
