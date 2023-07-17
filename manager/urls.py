from django.urls import path

from .views import base_views, reserve_views, consulting_views, student_study_views, patrol_views, report_views, \
    data_views

app_name = 'manager'

urlpatterns = [
    path('', base_views.index, name='index'),

    # reserve
    path('reserve/', reserve_views.reserve, name='reserve'),
    path('reserve/detail/<int:teacher_id>', reserve_views.reserve_detail, name='reserve_detail'),
    path('reserve/detail/<int:teacher_id>/<str:date>', reserve_views.reserve_detail_teacher,
         name='reserve_detail_teacher'),
    path('reserve/update/<int:reserve_id>/', reserve_views.reserve_update, name='reserve_update'),
    path('reserve/create/', reserve_views.reserve_create, name='reserve_create'),

    # consulting
    path('consulting/', consulting_views.consulting, name='consulting'),
    # 이거 검색에 따라서 url변동되도록 짜야할듯
    path('consulting/detail', consulting_views.consulting, name='consulting_detail'),

    # student_study
    path('student_study/', student_study_views.student_study, name='student_study'),
    path('student_study/detail', student_study_views.student_study_detail, name='student_study_detail'),
    path('student_study/upload/success', student_study_views.student_study_upload_success,
         name='student_study_upload_success'),
    path('student_study/upload/fail', student_study_views.student_study_upload_fail, name='student_study_upload_fail'),

    # patrol
    path('patrol/', patrol_views.patrol, name='patrol'),
    path('patrol/student_detail', patrol_views.patrol_student_detail, name='patrol_student_detail'),
    path('patrol/upload/success', patrol_views.patrol_upload_success, name='patrol_upload_success'),
    path('patrol/upload/fail/', patrol_views.patrol_upload_fail, name='patrol_upload_fail'),

    # data
    path('data/', data_views.index, name='data'),
    path('data/create/week/patrol/data/', data_views.create_week_patrol_data, name='create_week_patrol_data'),
    path('data/create/total/study/data/', data_views.create_total_study_data, name='create_total_study_data'),
    path('data/create/average/patrol/data/', data_views.create_average_patrol_data, name='create_average_patrol_data'),
    path('data/success/', data_views.patrol_weekly_data_success, name='patrol_weekly_data_success'),

    # report -> study
    path('report/', report_views.report_study_main, name='report_study_main'),
    path('report/detail/', report_views.report_study_detail, name='report_study_detail')

    # report -> grade

    # report -> consulting
]
