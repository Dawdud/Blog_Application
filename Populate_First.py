import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'firstproject.settings')
import django
django.setup()
from first.models import  Category, Books

def populate():
    FantasticBooks=[{"Title":"Straz Nocna", "OriginalTitle":"Night Watch", "Author":"Terry Pratchett", "ISBN":"9788378390909",
                     "Publisher":"Proszynski Media"}]
    ScienceFictionBooks=[{"Title":"Eden", "OriginalTitle":"Eden", "Author":"Stanislaw Lem","ISBN":"9788375224109",
                          "Publisher":"Jerzy Jarzebski and wydawnicto literackie"}]
    HorrorBooks=[{"Title":"Carrie","OriginalTitle":"Carrie", "Author":"Stephen King","ISBN":"9788378396314", "Publisher":"Proszynski Media"} ]
    cats={"Fantastic": {"books":FantasticBooks},
          "ScienceFiction":{"books":ScienceFictionBooks},
          "HorrorBooks":{"books": HorrorBooks}}
    for cat, cat_data in cats.items():
        c= add_cat(cat)
        for b in cat_data["books"]:
            add_book(c, b["Title"],b["OriginalTitle"],b["Author"],b["ISBN"], b["Publisher"])

    for c in Category.objects.all():
        for b in Books.objects.filter(category=c):
            print("-{0}-{1}".format(str(c),str(b)))

def add_book(cat, Title,OriginalTitle,Author,ISBN,Publisher):
        b = Books.objects.get_or_create(category= cat, Title= Title)[0]
        b.OriginalTitle= OriginalTitle
        b.Author= Author
        b.ISBN= int(ISBN)
        b.Publisher= Publisher
        b.save()
        return b
def add_cat(name):
    c= Category.objects.get_or_create(name=name)[0]
    c.save()
    return c
if __name__=='__main__':
    print("starting population script...")
    populate()
