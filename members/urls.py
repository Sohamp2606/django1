
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('members/',views.members,name='members'),
    path('members/details/<slug:slug>',views.details,name='details'),
    path('testing/',views.testing,name='test'),
]