import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Person
p=Person(
    first_name="Taro",last_name="Sato",
    birthday="2000-01-01",email="aa@mail.com",
    salary=None,memo="memo taro",web_site="http://www.google"
)
p=Person(
    first_name="Taro",last_name="Sato",
    birthday="2000-01-01",email="aa@mail.com",
    salary=None,memo="memo taro",web_site=""
)
p.save()