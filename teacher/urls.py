from django.urls import path

from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve_history/<int:teacher_id>', views.reserve_history, name='reserve_history'),
    path('reserve_history/<int:teacher_id>/<str:date>/', views.reserve_history_detail, name='reserve_history_detail'),

    path('consulting_page/', views.consulting_page, name='consulting_page'),
    path('consulting_detail/<int:consulting_id>', views.consulting_detail, name="consulting_detail"),
    path('consulting_create/', views.consulting_create, name="consulting_create"),
]












