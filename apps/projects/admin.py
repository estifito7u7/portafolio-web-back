from django.contrib import admin
from .models import Projects

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'github_link', 'website_link', 'date_created')
    list_display_links = ('id', 'name')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')
    list_per_page = 25

admin.site.register(Projects, ProjectsAdmin)
