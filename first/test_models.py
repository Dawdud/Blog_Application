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
    def test_string_repersentation(self):
        category_name = Category(name="Science Fiction")
        self.assertEqual(str(category_name), category_name.name)

class BookModelTest(TestCase):

    def test_slug_book(self):
        cat = Category.objects.create(name="HorrorBooks")
        book = Books.objects.create(Title="asf saf", OriginalTitle= "asf saf", Author="kowalski", Publisher="Media", category= cat)
        book.save()
        self.assertEqual(book.slugbook, 'asf-saf')
    def test_string_representation(self):
        book_name = Books(Title="Night Watch")
        self.assertEqual(str(book_name), book_name.Title)