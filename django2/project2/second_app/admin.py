from django.contrib import admin
from second_app.models import student
from second_app.models import classroom
from second_app.models import marks
from second_app.models import teachers
admin.site.register(student)

admin.site.register(classroom)
admin.site.register(marks)
admin.site.register(teachers)