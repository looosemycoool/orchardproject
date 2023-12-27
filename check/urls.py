from django.urls import path
from .views import attendence_views, base_views, register_views, create_book_views

app_name = 'check'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('register/', register_views.student_register, name='student_register'),
    path('create_book/', create_book_views.create_book, name='create_book'),
    path('attendences/p_class', attendence_views.attendance_index_p, name='attendance_index_p'),
    path('attendences/s_class', attendence_views.attendance_index_s, name='attendance_index_s'),

    path('attendences/p_class/<int:attendance_id>/', attendence_views.attendance_p, name='attendance_p'),
    path('attendences/s_class/<int:attendance_id>/', attendence_views.attendance_s, name='attendance_s'),
]