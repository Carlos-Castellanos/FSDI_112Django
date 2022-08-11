from django.urls import path
from .views import HomePageView, AboutPageView, About2PageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('about2/',About2PageView.as_view(),name='about2'),
    ]