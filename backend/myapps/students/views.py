from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def home(request):
    students = []
    return JsonResponse(students, safe=False)


def detail(request, student_id=None):
    student = dict()
    student['student_id'] = student_id
    return JsonResponse(student)
