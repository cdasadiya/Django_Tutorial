"""
URL configuration for project_django_tutorials project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('todo/',views.todo), # Register all the project level views 
    path('app1/', include('application1.urls')), # registering the applcation into project 
    path('application2/', include('application2.urls')), # registering the applcation into project 
    path('dynamic_view/', include('dynamic_view_app.urls')), # registering the applcation into project 
    path('', include('todo_app.urls')), # Changes For To Do Apps : registering the applcation into project 
]
