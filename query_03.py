import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.all())

# 件数
print(Students.objects.count())
print(Students.objects.filter(name="太郎").count())