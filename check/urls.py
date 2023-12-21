from django.urls import path
from .views import attendence_views, patrol_views, base_views

app_name = 'check'

urlpatterns = [
    path('', base_views.index, name='index'),
]