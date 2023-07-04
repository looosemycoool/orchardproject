from django.urls import path

from .views import base_views, reserve_views, consulting_views, student_study_views, patrol_views

app_name = 'manager'

urlpatterns = [
    path('', base_views.index, name='index'),
    # reserve
    path('reserve/', reserve_views.reserve, name='reserve'),
    path('reserve/create/', reserve_views.reserve_create, name='reserve_create'),
    path('reserve/detail', reserve_views.reserve_detail, name='reserve_detail'),

    # consulting
    path('consulting/', consulting_views.consulting, name='consulting'),
    # 이거 검색에 따라서 url변동되도록 짜야할듯
    path('consulting/detail', consulting_views.consulting, name='consulting_detail'),

    # student_study
    path('student_study/', student_study_views.student_study, name='student_study'),
    path('student_study/detail', student_study_views.student_study_detail, name='student_study_detail'),
    path('student_study/upload/success', student_study_views.student_study_upload_success, name='student_study_upload_success'),
    path('student_study/upload/fail', student_study_views.student_study_upload_fail, name='student_study_upload_fail'),

    # patrol
    path('patrol/', patrol_views.patrol, name='patrol'),
    path('patrol/student_detail', patrol_views.patrol_student_detail, name='patrol_student_detail'),
    path('patrol/upload/success', patrol_views.patrol_upload_success, name='patrol_upload_success'),
    path('patrol/upload/fail/', patrol_views.patrol_upload_fail, name='patrol_upload_fail'),
]
