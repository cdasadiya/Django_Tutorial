from django.urls import path
from . import views

urlpatterns = [
    path('<str:topics>',views.dynamic_views), # registering the applcation into project
]
