from django.db import models
from django.test import TestCase

from first.models import Category, Books

class CategoryModelTest(TestCase):
    def test_Category_Model(self):
        self.assertTrue(Category.objects.create(name='new thriller'))

    def Category_slug_test(self):
        cat= Category.objects.create(name="new thriller")
        cat.save()
        self.assertEqual(cat.slug, 'new-thriller')

class BookModelTest(TestCase):

    def test_slug_book(self):
        cat = Category.objects.create(name="HorrorBooks")
        book = Books.objects.create(Title="asf saf", OriginalTitle= "asf saf", Author="kowalski", Publisher="Media", category= cat)
        book.save()
        self.assertEqual(book.slugbook, 'asf-saf')
