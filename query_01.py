import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students

# 全件取得
print(Students.objects.all())