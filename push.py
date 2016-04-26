#!/usr/bin/python
import os,sys
sys.path.append('/home/feng/wyc/django/sblog')
os.environ['DJANGO_SETTINGS_MODULE']='djobs.settings'
from django.core.management import setup_environ
from djobs import settings
from simpleblog import models
setup_environ(settings)
def addAuthor(getname,getemail='',getwebsite=''):
    p=models.Author(name=getname,email=getemail,website=getwebsite)
    p.save()

addAuthor('rain','rain@163.com')

