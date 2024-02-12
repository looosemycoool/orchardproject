from django.urls import path

from .views import base_views, planner_views

app_name = 'mypage'

urlpatterns = [
    # base_views
    path('<int:user_id>/', base_views.index, name='index'),
    # path('detail/<int:teacher_id>/', base_views.detail, name='detail'),
    # path('register/', base_views.notice_register, name='register'),

    # planner_views
    path('<int:user_id>/planner/', planner_views.index, name='planner_index'),
    path('<int:user_id>/planner/search', planner_views.search, name='planner_search'),
    path('<int:user_id>/planner/detail/<str:date>', planner_views.detail, name='planner_detail'),
    #
    # # comment_views
    # path('comment_create/<int:reserve_id>', comment_views.comment_create, name='comment_create'),
    # path('comment_modify/<int:reserve_id>', comment_views.comment_modify, name='comment_modify'),
    #
    # # consult_views
    # path('consult_create/<int:reserve_id>', consult_views.consult_create, name='consult_create'),
    # path('consult_modify/<int:reserve_id>', consult_views.consult_modify, name='consult_modify')
]
