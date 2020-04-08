from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
	path('contact/', views.contact, name='contact'),
	path('blog-details/', views.blogdetails, name='blog-details'),
	path('blog/', views.blog, name='blog'),
	path('price/', views.price, name='price'),
	path('service/', views.service, name='service'),
	path('about/', views.about, name='about'),
	path('appointment/', views.appointment, name='appointment'),
]