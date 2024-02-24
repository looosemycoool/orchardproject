from django.urls import path

from .views import study_views, question_views, consulting_views, newstudy_views, word_views, mypage_search_views

app_name = 'report'

urlpatterns = [
    # study_views
    path('study/', study_views.index, name='study_index'),
    path('study/report/<int:student_id>', study_views.study_report, name='study_report'),

    # question_views
    path('question/', question_views.index, name='question_index'),
    path('question/report/<int:student_id>', question_views.question_report, name='question_report'),

    # consulting_views
    path('consulting/', consulting_views.index, name='consulting_index'),
    path('consulting/report/<int:student_id>', consulting_views.consulting_report, name='consulting_report'),

    # newstudy_views
    path('newstudy/', newstudy_views.index, name='newstudy_index'),
    path('newstudy/report/<int:student_id>', newstudy_views.newstudy_report, name='newstudy_report'),

    # word_views
    path('word/', word_views.index, name='word_index'),
    path('word/report/<int:student_id>', word_views.word_report, name='word_report'),

    # mypage_search_views
    path('mypage/', mypage_search_views.index, name='mypage_search_index'),
    path('mypage/detail/<int:student_id>', mypage_search_views.mypage_search_detail, name='mypage_search_detail')
]
