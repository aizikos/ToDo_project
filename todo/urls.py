"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import *
from homework.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path("test/", test, name="test"),
    path("work/",work,name="work"),
    path("habits/", habits,name="habits"),
    path("works/",works,name="works"),
    path("add-todo/",add_todo,name="add-todo"),
    path("delete_todo/<id>/",delete_todo,name="delete_todo"),
    path("mark-todo/<id>/",mark_todo,name="mark-todo"),
    path("meet/",meet,name="meet"),
    path("add-todos/",add_todos,name="add-todos"),
    path("add-habits/",add_habits,name="add-habits"),
    
    
]   + static(settings.STATIC_URL,document_root= settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
