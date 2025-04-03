from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import HeroSection, Project, Certificate, Course, Skill, AboutMe,College,Organizer

# Define resources for all models
class HeroSectionResource(resources.ModelResource):
    class Meta:
        model = HeroSection

class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project

class CertificateResource(resources.ModelResource):
    class Meta:
        model = Certificate

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course

class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill

class AboutMeResource(resources.ModelResource):
    class Meta:
        model = AboutMe

# Apply ImportExportModelAdmin to all models
@admin.register(HeroSection)
class HeroSectionAdmin(ImportExportModelAdmin):
    resource_class = HeroSectionResource
    list_display = ('name', 'profession', 'contact_link')

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    list_display = ('title', 'url')


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    list_display = ('title', 'tag')

@admin.register(Skill)
class SkillAdmin(ImportExportModelAdmin):
    resource_class = SkillResource
    list_display = ('name',)

@admin.register(AboutMe)
class AboutMeAdmin(ImportExportModelAdmin):
    resource_class = AboutMeResource
    list_display = ('bio',)


@admin.register(Certificate)
class CertificateAdmin(ImportExportModelAdmin):
    resource_class = CertificateResource
    list_display = ('title', 'tag')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["college"].widget.can_add_related = True  # Enables the Plus (+) icon
        form.base_fields["organizer"].widget.can_add_related = True  # Enables the Plus (+) icon
        return form

admin.site.register(College)
admin.site.register(Organizer)