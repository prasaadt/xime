from django.urls import path
import students
from students import views

urlpatterns = [
    path('login/',students.views.slogin,name='login'),
    path('name/',students.views.studentview,name='sview')

]