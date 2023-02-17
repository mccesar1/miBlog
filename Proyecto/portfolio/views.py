from django.shortcuts import render
from .models import Project, Certificaciones

# Create your views here.
def home(request):
    proyectos = Project.objects.all()
    certificaciones =  Certificaciones.objects.all()
    return render(request, 'index.html',{'proyectos': proyectos, 'certificaciones': certificaciones})