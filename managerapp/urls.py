from . import views
from django.urls import path

urlpatterns = [
    path('new/', views.new, name='new'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
