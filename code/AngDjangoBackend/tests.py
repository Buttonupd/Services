from django.test import TestCase
from .models import Tutorial
from .views import tutorial_detail, tutorial_list_published, tutorial_list
from AngDjangoBackend import views
from django.urls import reverse



class TestModels(TestCase):
    def test_book_has_an_author(self):
        book = Tutorial.objects.create(title="The man in the high castle")
        philip = Tutorial.objects.create(description="Philip")
        juliana = Tutorial.objects.create(published=False)
        self.assertEqual(book.title, "The man in the high castle")
        self.assertEqual(book.published, False)




        