from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('about',views.aboutpage,name='about'),
    path('services',views.servicespage,name='services'),
    path('portfolio',views.portfoliopage,name='portfolio'),
    path('team',views.teampage,name='team'),
    path('contact',views.contactpage,name='contact'),
    path('form',views.formpage,name='form'),
    path('test',views.testpage,name='test'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
