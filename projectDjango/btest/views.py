from django.http import HttpResponse
from .models import projects,workingOn
from django.db.models import Q

def index(request):
  s1 = 'Список участий\r\n\r\n\r\n'
  for bb in workingOn.objects.select_related("project").select_related("worker"):
    s1 += str(bb.project.title) +'  '+ bb.worker.surname +  '\r\n'
  s2 = '\r\n\r\n\r\n\r\nСписок проектов\r\n\r\n'
  d={}
  for bb in workingOn.objects.select_related("project").select_related("worker"):
    if(bb.project.title in d.keys()):
        d[bb.project.title]+=", "+bb.worker.surname
    else:
       d[bb.project.title]=bb.worker.surname
  for key, value in d.items():
     s2+=key+": "+value
     s2+="\r\n"

  
  return HttpResponse(s1+s2, content_type='text/plain; charset=utf-8')






