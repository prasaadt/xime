from django.urls import path

import faculty.views

urlpatterns = [
    path('login/',faculty.views.flogin,name='login')
]