import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students

# 全件取得
# print(Students.objects.all())

# 頭5件取得
# print(Students.objects.all()[:5])

# 5件より後
# print(Students.objects.all()[5:])

# 5～7件目
# print(Students.objects.all()[5:8])
# print(Students.objects.all()[5:8].query)

# 1番最初の1件
# print(Students.objects.first())

# 等価のモノだけ絞り込む
print(Students.objects.filter(name="太郎").all())
print(Students.objects.filter(age="17").all())

