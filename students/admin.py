from django.contrib import admin

# Register your models here.
from students.models import students

class studentsadmin(admin.ModelAdmin):
    list_display = ['sroll_no','sname','slastname']

admin.site.register(students,studentsadmin)