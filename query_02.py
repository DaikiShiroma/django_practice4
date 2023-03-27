import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students,Person
# print(Students.objects.all())

ids=[49,50,51]
# print(Students.objects.filter(pk__in=ids).all())

# contain 部分一致
# print(Students.objects.filter(name__contains="三").all())

# is null
# p=Person(
#     first_name="Jiro",last_name="Yamada",
#     birthday="2000-01-01",email="aa@mail.com",
#     salary=1000,memo="memo taro",web_site="http://www.google"
# )
# p.save()

print(Person.objects.filter(salary__isnull=True).all())

# レコードを取り除く(filter =>　exclude)
print(Students.objects.exclude(name="太郎").all())
