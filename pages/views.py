# from django.shortcuts import render
from re import template
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
# Create your views here.
