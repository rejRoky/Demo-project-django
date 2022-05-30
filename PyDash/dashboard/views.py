from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Welcome to Dashboard')


def dispenseInfo(request):
    return HttpResponse('Welcome to Dispense Info')


def salesInfo (request):
    return HttpResponse('Welcome To Sales Info')


def deviceInfo(request):
    return HttpResponse('WelCome To Device Info')


def userInfo(request):
    return HttpResponse('Welcome to Device Info')


def rfidInfo(request):
    return HttpResponse('Welcome to REID Info')


