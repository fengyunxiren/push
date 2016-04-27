#!/usr/bin/python
import os,sys
sys.path.append('/home/feng/wyc/django/sblog')
os.environ['DJANGO_SETTINGS_MODULE']='djobs.settings'
from django.core.management import setup_environ
from djobs import settings
from simpleblog import models
setup_environ(settings)




def addAuthor(fname):
    f=open(fname)
    lines=f.readlines()
    for line in lines:
        spline=line.split(',')
        p=models.Author(name=spline[0],email=spline[1],website=spline[2])
        p.save()


def delAuthor(dname,demail='',dwebsite=''):
    try:
        p=models.Author.objects.get(name=dname,email=demail,website=dwebsite)
    except models.Author.DoesNotExist:
        print " Author name: %s,email: %s,website: %s dose not exist!!!" % (dname,demail,dwebsite)
    else:
        p.delete()
        print " Author name: %s,email: %s,website: %s deleted" % (dname,demail,dwebsite)


def addBlog(fname):
    f=open(fname)
    title=f.readline()
    line=f.readline()
    spline=line.split(':')
    if (spline[0]=='author'or spline[0]=='Author') and len(spline)>=2:
        try:
            pauthor=models.Author.objects.get(name=spline[1].strip('\n'))
            content=f.read()
            blog=models.Blog(caption=title,author=pauthor,content=content)
            blog.save()
        except models.Author.DoesNotExist:
            print "Author name:%s does not exist!!!" % spline[1].strip('\n')
        else:
            print "Author name right"
    else:
        try:
            pauthor=models.Author.objects.get(name=line.strip('\n'))
            content=f.read()
            blog=models.Blog(caption=title,author=pauthor,content=content)
        except models.Author.DoesNotExist:
            print "Author name:%s** does not exist!!!" % line.strip('\n')
        else:
            print "Author name right"
    f.close()
        
#addAuthor('author.txt')
#delAuthor('rin','rain@163.com')
addBlog('blog.txt')
