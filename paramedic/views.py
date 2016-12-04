from django.shortcuts import render
from django.http import HttpResponse
from paramedic.models import Hospital
from paramedic.models import Patient
from paramedic.models import MedicalInstr
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")
'''
def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
'''

def paramedic_home(request):
    return render(request, 'paramedic_home.html', {'title': 'menu'})

def paramedic_patientinfo(request):
    return render(request, 'patient_info.html', {'title': 'patient'})

def paramedic_info_detail(request):
    return render(request, 'patient_info_detail.html',{'title': 'patient'})

def paramedic_hospital(request):
    return render(request, 'hospital.html', {'title': 'hospital'})

def paramedic_map(request):
    return render(request, 'map.html', {'title': 'map'})

def paramedic_instruction(request):
    return render(request, 'druglist.html', {'title': 'instruction'})

def paramedic_list(request):
    return render(request, 'druglist.html', {'title': 'instruction'})

def report(request) :
    return render(request, 'report.html', {'title': 'report'})