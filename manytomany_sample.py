import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Books,Authors

def insert_books():
    book1=Books(name="Book1")
    book2=Books(name="Book2")
    book3=Books(name="Book3")
    book1.save()
    book2.save()
    book3.save()

def insert_authors():
    authors1=Authors(name="Author1")
    authors2=Authors(name="Author2")
    authors3=Authors(name="Author3")
    authors1.save()
    authors2.save()
    authors3.save()

# insert_books()
# insert_authors()

book1=Books.objects.get(pk=1)
book3=Books.objects.get(pk=3)

authors1=Authors.objects.get(pk=1)
authors2=Authors.objects.get(pk=2)
authors3=Authors.objects.get(pk=3)

# book1.authors.add(authors1,authors2)

# print(book1.authors.all())
book3.authors.add(authors1)
book3.authors.add(authors2,authors3)

