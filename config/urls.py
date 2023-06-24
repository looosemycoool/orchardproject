from django.contrib import admin
from django.urls import path, include
from reserve.views import base_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('reserve/', include('reserve.urls')),
    path('common/', include('common.urls')),
    path('teacher/', include('teacher.urls')),
    path('manager/', include('manager.urls')),

    path('', base_views.index, name='index'),    # '/' 에 해당되는 path
]

handler404 = 'common.views.page_not_found'
