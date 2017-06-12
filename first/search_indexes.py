from haystack import indexes
from first.models import Books

class BooksIndex(indexes.SearchIndex, indexes.Indexable):

    text= indexes.CharField(document=True, use_template=True)
    category= indexes.CharField(model_attr='category')
    Title= indexes.CharField(model_attr='Title')
    OriginalTitle= indexes.CharField(model_attr='OriginalTitle')
    Author= indexes.CharField(model_attr='Author')
    Publisher= indexes.CharField(model_attr='Publisher')
    slugbook= indexes.CharField(model_attr='slugbook')
    id= indexes.IntegerField(model_attr='id')
    def get_model(self):
        return Books
    def index_queryset(self, using=None):
        return self.get_model().objects.all()