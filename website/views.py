from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class GetIndexView(TemplateView):
    template_name = "index.html"
