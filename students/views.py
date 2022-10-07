""" from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!") """

""" from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('eventshome.html')
  return HttpResponse(template.render()) """

""" from django.http import HttpResponse
from django.template import loader
from .models import EventsTb

def index(request):
  myevents = EventsTb.objects.all().values()
  output = ""
  for x in myevents:
    output = output + "<br>" + x["EventName"]
  return HttpResponse(output) """
  
 
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import EventsTb

def index(request):
  myevents = EventsTb.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mycourses': myevents,
  }
  return HttpResponse(template.render(context, request))

def courses(request):
  myevents = EventsTb.objects.all().values()
  template = loader.get_template('courses.html')
  context = {
    'mycourses': myevents,
  }
  return HttpResponse(template.render(context, request))

def addcourse(request):
  template = loader.get_template('addcourse.html')
  return HttpResponse(template.render({}, request))

def addcoursetodb(request):
  eventname = request.POST['txtEventName']
  eventdesc = request.POST['txtEventDesc']
  event = EventsTb(EventName=eventname, EventDesc=eventdesc)
  event.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  event = EventsTb.objects.get(id=id)
  event.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mycourse = EventsTb.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mycourse': mycourse,
  }
  return HttpResponse(template.render(context, request))

def updatecourse(request, id):
  eventname = request.POST['txtEventName']
  eventdesc = request.POST['txtEventDesc']
  course = EventsTb.objects.get(id=id)
  course.EventName = eventname
  course.EventDesc = eventdesc
  course.save()
  return HttpResponseRedirect(reverse('index'))