from django.contrib import admin
from .models import workers,workingOn,projects
admin.site.register(workers)
admin.site.register(workingOn)
admin.site.register(projects)
