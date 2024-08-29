from django.shortcuts import render,HttpResponse
from .models import Info, Skills, Links, Experience, Projects
# Create your views here.

def home(request):
    info = Info.objects.first()
    skills = Skills.objects.all()
    links = Links.objects.first()
    experience = Experience.objects.all()
    projects  = Projects.objects.all()
    context = {
        'info': info,
        'skills': skills,
        'links': links,
        'experience': experience,
        'projects': projects,
    }
    return render(request, 'index.html', context)