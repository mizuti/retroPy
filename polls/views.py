from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello kyle, you are almost there. Keep going')
