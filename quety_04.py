import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Students,schools

# for student in Students.objects.all():
#     print(student.name,student.school.name,student.school.prefecture.name)

# 外部テーブルでフィルター
# for student in Students.objects.filter(school__name="南高校").all():
#     print(student.name,student.school.name,student.school.prefecture.name)    

# 外部テーブルで取り除く
# for student in Students.objects.exclude(school__name="南高校").all():
#     print(student.name,student.school.name,student.school.prefecture.name)

# print(schools.objects.filter(students__name="太郎").all().query)

print("-"*100)

# 並び替え
for student in Students.objects.order_by("school__name").all():
    print(student.name,student.school.name)

# GROUP BY
from django.db.models import Count,Max
print(Students.objects.values("school__name").annotate(Count("id"),Max("id")))