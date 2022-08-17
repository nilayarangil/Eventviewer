from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('admin/', views.index, name='index'),
    path('addnewcourse/', views.addcourse, name='addcourse'),
    path('addnewcourse/addcoursetodb/', views.addcoursetodb, name='addcoursetodb'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updatecourse/<int:id>', views.updatecourse, name='updatecourse'),
]

