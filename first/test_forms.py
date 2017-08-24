from django.test import TestCase
from first.forms import CategoryForm, BookForm, SignUpForm

class CategoryTest(TestCase):
    def test_Category_valid(self):
        form= CategoryForm(data={'name':'Comic'})
        self.assertTrue(form.is_valid())
    def test_Category_Invalid(self):
        form= CategoryForm(data={'name':''})
        self.assertFalse(form.is_valid())


class BookTest(TestCase):
    def test_books_valid(self):
        form= BookForm(data={'Title': 'Igrzyska smierci','OriginalTitle':'Hunger Games', 'Author': 'Suzanne Collins', 'Publisher':'Rodzina', 'ISBN':'9788372786371', 'DatePublished':'2017-09-05' })
        self.assertTrue(form.is_valid())
    def Test_books_invalid_one(self):
        form = BookForm(data={'Title': '', 'OriginalTitle': '', 'Author': '',
                              'Publisher': '', 'ISBN': 'asfd', 'DatePublished':''})
        self.assertFalse(form.is_valid())

