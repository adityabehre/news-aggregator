from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
  return HttpResponse("<strong>Segz</strong> page for <strong>segz</strong> news")
