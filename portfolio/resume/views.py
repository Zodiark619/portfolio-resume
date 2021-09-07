from django.shortcuts import render
from resume.models import *

summary="""
I'm a fresh graduate with bachelor degree in computer science.
I'm a self-taught python programmer.
I'm interested in learning new things and increasing my knowledge relevant to python
programming language and other information technology.
"""
title='Resume'
name='Herry Wijaya'
occupation='Full Stack Web Developer'
address='Bogorpark Residence Blok D27 Pamoyanan, Bogor, Jawa Barat'
email='herrywijaya065116076@unpak.ac.id'
telephone='0895632067037'
# Create your views here.
def index(request):
    a=list(skill.objects.all())
    b=list(license.objects.all())
    c=list(experience.objects.all())
    d=list(education.objects.all())
    return render(request,'resume/index.html',{'title':title,'name':name,
                                                'occupation':occupation,
                                                'address':address,
                                                'email':email,
                                                'telephone':telephone,
                                                'a':a,
                                                'summary':summary,
                                                'b':b,
                                                'c':c,
                                                'd':d
                                            })
