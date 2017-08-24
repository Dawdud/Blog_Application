from django.test import TestCase
from django.contrib.auth.models import User
from first.models import  Books, Category


class AboutTest(TestCase):
    def test_about(self):
        resp= self.client.get('/first/about/')
        self.assertEqual(resp.status_code,200)


class AddCategory(TestCase):
    def setUp(self):
        User.objects.create_superuser('usertest', 'usertest@mail.com','password')
        self.client.login(username="usertest", password="password")
    def tearDown(self):
        self.client.logout()
    def test_addcategory(self):
        response = self.client.get("/first/add_category/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'first/add_category.html')


class AddBooks(TestCase):

    def setUp(self):
        User.objects.create_superuser('usertest', 'usertest@mail.com','password')
        self.client.login(username="usertest", password="password")
    def tearDown(self):
        self.client.logout()
    def test_addbooks(self):
        c = Category.objects.create(name="Comic")
        c.save()

        response= self.client.get("/first/category/%s/add_books/"%c.slug)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'first/add_books.html')


class LogoutTest(TestCase):
    def test_logout(self):

        resp= self.client.get('/first/logout/')
        self.assertEqual(resp.status_code, 200)




class indexTest(TestCase):
     def test_index(self):
         resp= self.client.get('/first/')
         self.assertEqual(resp.status_code, 200)
         self.assertTemplateUsed(resp, 'first/index.html')

class TestshowCategory(TestCase):
    def test_CategoryShow(self):
        c = Category.objects.create(name= "Comic" )
        c.save()
        resp=  self.client.get('/first/category/%s/' % c.slug)
        self.assertEqual(resp.status_code, 200)


class ShowBooksTest(TestCase):
    def test_BooksShow(self):
        cat = Category.objects.create(name="HorrorBooks")
        book = Books.objects.create(Title="asf saf", OriginalTitle= "asf saf", Author="kowalski", Publisher="Media", category= cat)
        book.save()
        resp= self.client.get('/first/book/%s/%s'%(book.id, book.slugbook))
        self.assertEqual(resp.status_code, 200)