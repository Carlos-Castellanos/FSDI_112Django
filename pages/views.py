# from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"



class About2PageView(TemplateView):
    template_name = "about2.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mename'] = "Carlos Alberto Lopez"
        context['description'] = "I am a teacher but now I am learning django, and this is a jinja templates example"
        return context


