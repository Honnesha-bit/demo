from django.urls import path
from . import views

urlpatterns = [
    path('studeny_forms/',views.student_form,
         name='stuent_form'),
]