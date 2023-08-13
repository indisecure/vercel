from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Customer,Table
from django.contrib import messages
def course(r):
    table=Table.objects.all()
    return render(r,'course.html',{'table':table})
def index(r):
    return render(r,'index.html',{})
def alumni(r):
    return render(r,'alumni.html',{})
def c(r):
    return render(r,'c.html',{})
def web(r):
    return render(r,'web.html',{})
def java(r):
    return render(r,'java.html',{})
def python(r):
    return render(r,'python.html',{})
def leads(r):
    customer=Customer.objects.all()
    return render(r,'leads.html',{'customer':customer})
def sitemap(r):
    return render(r,'sitemap.xml')
def robot(r):
    return render(r,'robots.txt')

def contact(r):
    if r.method=='POST':
        if r.POST['name']and r.POST['email']and r.POST['mobile'] and r.POST['message']:
            model=Customer(name=r.POST['name'],email=r.POST['email'],mobile=r.POST['mobile'],message=r.POST['message'])
            model.save()
            messages.info(r, mark_safe('Message Received,Thanks,We Will Contact You asap!'))
            return render(r,'contact.html',{})
    else:
        return render (r,'contact.html',{})