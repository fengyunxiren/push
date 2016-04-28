import sqlite3
import sys
import datetime


def push(fname):
    cx=sqlite3.connect("/home/feng/wyc/django/sblog/datas/mydata.db")
    cu=cx.cursor()
    f=open(fname)
    title=f.readline().strip('\n')
    line=f.readline().strip('\n')
    spline=line.split(':')
    if (spline[0]=='author' or spline[0]=='Author') and len(spline)>=2:
        cu.execute("select * from simpleblog_author where name='%s'" % spline[1])
        author=cu.fetchone()
        if not author:
            print "ERROR:Author name:%s does not exist!!!" % spline[1]
            sys.exit(1)
    else:
        cu.execute("select * from simpleblog_author where name='%s'" % line)
        author=cu.fetchone()
        if not author:
            print "ERROR:Author name:%s does not exist!!!" % line
            sys.exit(1)
    content=f.read()
    title=unicode(title,"utf-8")
    content=unicode(content,"utf-8")
    cu.execute("select id from simpleblog_blog")
    id=max(cu.fetchall())[0]+1
    zz=datetime.datetime.now()
    cu.execute("insert into simpleblog_blog values('%d','%s','%d','%s','%s','%s')" % (id,title,author[0],content,zz,zz))
    cx.commit()
    cu.close()
    cx.close()
    print "Blog push successful"


        
##########################################################
push('blog.txt')
