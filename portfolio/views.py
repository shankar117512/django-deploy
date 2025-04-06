from django.shortcuts import redirect,render
from app.models import HeroSection,Project,Certificate,Course,AboutMe,Skill
from collections import defaultdict 


def BASE(request):
    hero_section = HeroSection.objects.first()
    projects = Project.objects.all()
    certificates = Certificate.objects.all()[:3]
    courses = Course.objects.all()
    about_me = AboutMe.objects.first() 
    skills = Skill.objects.all()
    context = {
        "hero_section":hero_section,
        "projects": projects,
        'certificates':certificates,
        'courses':courses,
        'about_me':about_me,
        'skills':skills

    }
    return render(request,'Main/home.html',context)

def CERTIFICATE(request):
    certificates = Certificate.objects.order_by('-id') # No filtering by issued_date
    return render(request, "Certificate/certificate.html", {'certificates': certificates})
