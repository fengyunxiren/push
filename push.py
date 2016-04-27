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
        line.strip('\n')
        spline=line.split(',')
        p=models.Author(name=spline[0],email=spline[1],website=spline[2])
        p.save()


def delAuthor(dname,demail='',dwebsite=''):
    try:
        p=models.Author.objects.get(name=dname,email=demail,website=dwebsite)
    except models.Author.DoesNotExist:
        print "ERROR:Author name: %s,email: %s,website: %s dose not exist!!!" % (dname,demail,dwebsite)
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
            print "ERROR:Author name:%s does not exist!!!" % spline[1].strip('\n')
        else:
            print "Author name right"
    else:
        try:
            pauthor=models.Author.objects.get(name=line.strip('\n'))
            content=f.read()
            blog=models.Blog(caption=title,author=pauthor,content=content)
        except models.Author.DoesNotExist:
            print "ERROR:Author name:%s** does not exist!!!" % line.strip('\n')
        else:
            print "Author name right"
    f.close()
        

def delBlog(dtitle='',dauthor=''):
    if dtitle!='' and dauthor=='':
        try:
            blog=models.Blog.objects.get(caption=dtitle)
        except models.Blog.DoesNotExist:
            print "ERROR:Blog title=%s does not exist!!!" % dtitle

    elif dtitle=='' and dauthor!='':
        try:
            blog=models.Blog.objects.get(author=dname)
        except models.Blog.DoesNotExist:
            print "ERROR:Blog author=%s does not exist!!!" % dauthor

    elif dtitle!='' and dauthor!='':
        try:
            blog=models.Blog.objects.get(caption=dtitle,author=dauthor)
        except models.Blog.DoesNotExist:
            print "ERROR:Blog title=%s,author=%s does not exist!!!" % (dtitle,dauthor)

    else:
        print "Please input title name or author name or both of them"
        sys.exit(1)

    if blog:
        blog.delete()
        print "Blog deleted successful!"


def runPush():
    if sys.argv[0]=='python':
        if len(sys.argv)>2:
            if sys.argv[2]=='addauthor' or sys.argv[2]=='addblog':
                if len(sys.argv)!=4:
                    print "ERROR:Argument number wrong!!!"
                    print "Use: %s %s %s filename" % (sys.argv[0],sys.argv[1],sys.argv[2])
                    sys.exit(1)
                if sys.argv[2]=='addblog':
                    addBlog(sys.argv[3])
                else:
                    addAuthor(sys.argv[3])
            else:
                print "Argument wrong!!! Argument=addauthor or addblog"
                print "Use: %s %s addauthor/addblog filename" % (sys.argv[0],sys.argv[1])
                sys.exit(1)
        else:
            print "ERROR:Argument number wrong!!!"
            sys.exit(1)
    else:
        if len(sys.argv)>1:
            if sys.argv[1]=='addauthor' or sys.argv[1]=='addblog':
                if len(sys.argv)!=3:
                    print "ERROR:Argument number wrong!!!"
                    print "Use: %s %s filename" % (sys.argv[0],sys.argv[1])
                    sys.exit(1)
                if sys.argv[1]=='addblog':
                    addBlog(sys.argv[2])
                else:
                    addAuthor(sys.argv[2])
            else:
                print "Argument wrong!!! Argument=addauthor or addblog"
                print "Use: %s addauthor/addblog filename" % sys.argv[0]
                sys.exit(1)
        else:
            print "ERROR:Argument number wrong!!!"
            sys.exit(1)

#######################################################
runPush()
