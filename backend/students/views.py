from django.shortcuts import render
from .forms import StudentForm
# def home(request):
#     return render(request, 'home.html')     

def student_form(request):
    form=StudentForm()
    return render(request,'studentds/student_forms.html',{form:form})   