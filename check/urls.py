from django.urls import path
from .views import attendence_views, base_views, student_views, create_book_views, patrol_views

app_name = 'check'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('update/<int:attendance_id>',base_views.update_attendance, name='update_attendance'),
    path('specify/', base_views.specify, name='specify'),

    #path('search/', base_views.search, name='search'),
    path('detail/<str:selected_date>', base_views.detail, name='detail'),
    #path('search/<str:selected_class>/<str:selected_date>/', base_views.search_result, name='search_result'),

    path('create_book/', create_book_views.create_book, name='create_book'),
    path('create_patrol/', create_book_views.create_patrol_book, name='create_patrol'),

    # attendance
    path('attendences/p_class', attendence_views.attendance_index_p, name='attendance_index_p'),
    path('attendences/s_class', attendence_views.attendance_index_s, name='attendance_index_s'),
    path('attendences/m_class', attendence_views.attendance_index_m, name='attendance_index_m'),

    # patrol
    path('patrol/', patrol_views.index, name='patrol'),

    path('patrol/p_class', patrol_views.patrol_p_class, name='patrol_p_class'),
    path('patrol/p_class/<int:patrol_id>', patrol_views.patrol_check_p, name='patrol_check_p'),

    path('patrol/s_class', patrol_views.patrol_s_class, name='patrol_s_class'),
    path('patrol/s_class/<int:patrol_id>', patrol_views.patrol_check_s, name='patrol_check_s'),

    # student
    path('student/', student_views.index, name='student'),
    path('student/register/', student_views.register, name='register'),
    path('student/modify/<int:student_id>', student_views.modify, name='modify'),
    path('students_list', student_views.students_list, name='students_list')
]