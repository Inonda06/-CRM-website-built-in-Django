from unicodedata import name
from venv import create
from django.urls import path
from .import views

app_name= "leeds"
urlpatterns =[
    path("Lead list/",views.Lead_List, name= 'homepage'),
    path("details/<str:pk>/",views.Lead_details, name= 'details'),
    path("Create/", views.Lead_Create, name= "create"),
    path("Update/<str:pk>/", views.Lead_update, name= 'Update'),
    path("delete/<str:pk>/",views.Lead_delete,name= 'delete'),
]