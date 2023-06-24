from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from reserve.models import Reserve, Teacher, Notice

@login_required(login_url='common:login')
@user_passes_test(lambda u: u.is_staff, login_url="common:login")
def index(request):
    teacher_table = Teacher.objects.order_by('id')
    return render(request, 'teacher/reserve/reserve_main.html', {'teacher_table': teacher_table})