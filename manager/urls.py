from django.urls import path

from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.index, name='index'),
    # path('detail/<int:teacher_id>/', base_views.detail, name='detail'),
    #
    # path('complete/<int:reserve_id>/', reserve_views.reserve, name='complete'),
    # path('delete/<int:reserve_id>/', reserve_views.reserve_delete, name='delete'),
    #
    # path('comment_create/<int:reserve_id>', comment_views.comment_create, name='comment_create'),
    # path('comment_modify/<int:reserve_id>', comment_views.comment_modify, name='comment_modify')
]
