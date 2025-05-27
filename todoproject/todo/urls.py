
# from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    #  path('admin/', admin.site.urls),
    path('', views.index, name='list'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
]
