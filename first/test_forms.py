from django.test import TestCase
from first.forms import CategoryForm, BookForm

class CategoryTestCase(TestCase):
    def test_Category(self):
        form= CategoryForm(data={'name':'Comic','slug':'comic'})
        self.assertTrue(form.is_valid())
    def test_Category_Invalid(self):
        form= CategoryForm(data={'name':'', 'slug':''})
        self.assertFalse(form.is_valid())

class BookTestCase(TestCase):
    def test_books_valid(self):
        form= BookForm(data={'Title': 'Igrzyska smierci','OriginalTitle':'Hunger Games', 'Author': 'Suzanne Collins', 'Publisher':'Rodzina', 'ISBN':'9788372786371', 'DatePublished':'2017-09-05' })
        self.assertTrue(form.is_valid())
    def Test_books_invalid_one(self):
        form = BookForm(data={'Title': '', 'OriginalTitle': '', 'Author': '',
                              'Publisher': '', 'ISBN': 'asfd', 'DatePublished':''})
        self.assertFalse(form.is_valid())

