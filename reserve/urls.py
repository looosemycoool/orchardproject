from django.urls import path

from .views import base_views, reserve_views, comment_views

app_name = 'reserve'

urlpatterns = [
    # base_views
    path('', base_views.index, name='index'),
    path('detail/<int:teacher_id>/', base_views.detail, name='detail'),

    # reserve_views
    path('complete/<int:reserve_id>/', reserve_views.reserve, name='complete'),
    path('delete/<int:reserve_id>/', reserve_views.reserve_delete, name='delete'),

    # comment_views
    path('comment_create/<int:reserve_id>', comment_views.comment_create, name='comment_create'),
    path('comment_modify/<int:reserve_id>', comment_views.comment_modify, name='comment_modify')
]
