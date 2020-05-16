from django.contrib import admin
from projects.models import Project, About
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(About, AboutAdmin)
admin.site.register(Project, ProjectAdmin)
