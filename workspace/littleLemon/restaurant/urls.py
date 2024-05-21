#define URL route for index() view

from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView


urlpatterns = [
path('', views.home, name="home"),
path('about/', views.about, name="about"),
path('api-token-auth/', obtain_auth_token),
path('book/', views.book, name="book"),
path('menu/', views.menu, name="menu"),
path('menu/', views.MenuItemView.as_view()),
path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
path('',TemplateView.as_view(template_name='index.html'), name='indexpage'),
]
