"""
URL configuration for NewsPaper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from News_Portal.views import NewsListView, NewsDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='news/default.html'), name='home'),  # Домашняя страница
    path('about/', TemplateView.as_view(template_name='news/about.html'), name='about'),  # Страница "О сайте"
    path('contact/', TemplateView.as_view(template_name='news/contact.html'), name='contact'),  # Страница контактов
    path('news/', NewsListView.as_view(), name='news_list'),  # Список всех новостей
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Детали одной новости
]
