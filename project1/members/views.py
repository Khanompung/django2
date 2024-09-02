from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def members(request):
  template = loader.get_template('members.html')
  return HttpResponse(template.render())

def profile(request):
  template = loader.get_template('profile.html')
  return HttpResponse(template.render())