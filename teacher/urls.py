from django.urls import path
from .views import consulting_views, reserve_views, base_views

app_name = 'teacher'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('reserve_history/<int:teacher_id>', reserve_views.reserve_history, name='reserve_history'),
    path('reserve_history/<int:teacher_id>/<str:date>/', reserve_views.reserve_history_detail, name='reserve_history_detail'),

    path('reserve_history/create/<int:reserve_id>', reserve_views.consult_create, name='consult_create'),
    path('reserve_history/modify/<int:reserve_id>', reserve_views.consult_modify, name='consult_modify'),

    path('consulting_page/', consulting_views.consulting_page, name='consulting_page'),
    path('consulting_detail/<int:consulting_id>', consulting_views.consulting_detail, name="consulting_detail"),
    path('consulting_create/', consulting_views.consulting_create, name="consulting_create"),
]












