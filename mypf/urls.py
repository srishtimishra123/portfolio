from django.urls import path
from . import views #import views


# adding url
urlpatterns = [
    path('test', views.index, name='test'), #home
    path('portfolio', views.portfolio, name='portfolio'), #portfolio
    # path('contact', views.contact, name='contact'), #contact
    path('',views.test,name="home"),
    path('work',views.work,name="work"),
    path('contact',views.contact,name="contact"),
]