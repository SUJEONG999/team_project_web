import random
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

def main(request) :
    template = loader.get_template('main.html')
    return HttpResponse(template.render(None, request))

def map1(request) :
    template = loader.get_template('map1.html')
    return HttpResponse(template.render(None, request))

def map2(request) :
    template = loader.get_template('map2.html')
    return HttpResponse(template.render(None, request))

def board(request) :
    template = loader.get_template('board.html')
    return HttpResponse(template.render(None, request))

def register(request) :
    template = loader.get_template('register.html')
    return HttpResponse(template.render(None, request))

def login(request) :
    template = loader.get_template('login.html')
    return HttpResponse(template.render(None, request))

def logout(request) :
    template = loader.get_template('logout.html')
    return HttpResponse(template.render(None, request))