from django.urls import path
from . import views
urlpatterns = [
    path('',views.index), # registering the applcation into project
    path('second/',views.second), # registering the applcation into project
    
]
