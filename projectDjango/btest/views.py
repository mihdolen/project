from django.http import HttpResponse
from .models import projects,workingOn
from django.db.models import Q
from django.shortcuts import render

def index(request):

  wOns=workingOn.objects.select_related("project").select_related("worker")
  dprojects={}
  
  for bb in workingOn.objects.select_related("project").select_related("worker"):
    if(bb.project.title in dprojects.keys()):
        dprojects[bb.project.title]+=[bb.worker.surname + " " +  bb.worker.name + " " + bb.worker.otchestvo]
    else:
       dprojects[bb.project.title]=[bb.worker.surname + " " +  bb.worker.name + " " + bb.worker.otchestvo]


  
  return render(request, "btest/index.html",{'wOns': wOns, 'dprojects' : dprojects})






