from django.urls import path
from .views import attendence_views, base_views, register_views, create_book_views, patrol_views

app_name = 'check'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('update/<int:attendance_id>', base_views.update_attendance, name='update_attendance'),

    path('register/', register_views.student_register, name='student_register'),
    path('create_book/', create_book_views.create_book, name='create_book'),
    # attendance
    path('attendences/p_class', attendence_views.attendance_index_p, name='attendance_index_p'),
    path('attendences/s_class', attendence_views.attendance_index_s, name='attendance_index_s'),

    path('attendences/p_class/<int:attendance_id>/', attendence_views.attendance_p, name='attendance_p'),
    path('attendences/s_class/<int:attendance_id>/', attendence_views.attendance_s, name='attendance_s'),
    # patrol
    path('patrol/', patrol_views.index, name='patrol'),
    path('patrol/create_patrol/', patrol_views.create_patrol_book, name='create_patrol'),

    path('patrol/p_class', patrol_views.patrol_p_class, name='patrol_p_class'),
    path('patrol/p_class/<int:patrol_id>', patrol_views.patrol_check_p, name='patrol_check_p'),

    path('patrol/s_class', patrol_views.patrol_s_class, name='patrol_s_class'),
    path('patrol/s_class/<int:patrol_id>', patrol_views.patrol_check_s, name='patrol_check_s'),
]