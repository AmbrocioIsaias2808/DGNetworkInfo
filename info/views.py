from django.shortcuts import render
from .models import info_chart
from django.template import RequestContext
import random as rand
number=0
T=0
from django.http import request
# Create your views here.

def index(request):
    informacion=info_chart.objects.all()
    return render(request,"info/index.html",{"conceptos":informacion})


def random(request):
    global number,T
    context=RequestContext(request)
    T=len(info_chart.objects.all()) #T=total de registros
    print ("Total de registros:",T)
    concepto=select(T)
    number=concepto.concept_number
    return render(request,"info/aleatory.html",{"def":concepto},context)

def next(request):
    global number,T
    print ("T=",T)
    context = RequestContext(request)
    number = int(number) + 1
    if number>T:
        number=1
    entrada=number
    print ("entrada",entrada)
    concepto=info_chart.objects.get(concept_number=entrada)
    return render(request,"info/NEXT.html",{"def":concepto},context)

def back(request):
    global number,T
    print ("T=",T)
    context = RequestContext(request)
    number = int(number) - 1
    if number==0:
        number=T
    entrada=number
    print ("entrada",entrada)
    concepto=info_chart.objects.get(concept_number=entrada)
    return render(request,"info/NEXT.html",{"def":concepto},context)

def set_number():
    global number
    number=number;
def select(T):
    register=(rand.random()*T)+1
    concepto=info_chart.objects.get(concept_number=register)
    return concepto
