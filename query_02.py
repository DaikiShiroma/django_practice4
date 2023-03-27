import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students
# print(Students.objects.all())

ids=[49,50,51]
# print(Students.objects.filter(pk__in=ids).all())

# contain 部分一致
print(Students.objects.filter(name__contains="三").all())