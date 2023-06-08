
from django.contrib import admin
from django.urls import path
from . import views
app_name='crudapp'


urlpatterns = [
    path('',views.create,name='create'),
    path('delete/<int:itemid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    

]

