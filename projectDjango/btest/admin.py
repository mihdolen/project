from django.contrib import admin
from .models import workers,workingOn,projects

class workersAdmin(admin.ModelAdmin):
  list_display = ('surname', 'name', 'otchestvo', 'position')
  list_display_links = ('surname', 'name', 'otchestvo')
  search_fields = ('surname', 'name', 'otchestvo', 'position')


class workingOnAdmin(admin.ModelAdmin):
  list_display = ('worker','project')
  list_display_links = ('worker','project')

class projectsAdmin(admin.ModelAdmin):
  list_display = ('title', 'price', 'satrtDate', 'endDate')
  list_display_links = (['title'])
  search_fields = (['title'])

admin.site.register(workers,workersAdmin)
admin.site.register(workingOn,workingOnAdmin)
admin.site.register(projects,projectsAdmin)

