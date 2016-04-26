#!/usr/bin/python
import os,sys
sys.path.append('/home/feng/wyc/django/sblog')
os.environ['DJANGO_SETTINGS_MODULE']='djobs.settings'
from django.core.management import setup_environ
from djobs import settings
from simpleblog import models
setup_environ(settings)

p1=models.Author(name='cheetah',email='cheetah@163.com')
p1.save()
