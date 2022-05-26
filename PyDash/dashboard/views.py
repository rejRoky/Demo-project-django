from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Welcome to Dashboard')


def summary(request):
    return HttpResponse('Summary Page')


