from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Reserve, Teacher, Notice

from datetime import date

@login_required(login_url='common:login')
def index(request):
    teacher_table = Teacher.objects.order_by('id')
    teacher = Teacher.objects.order_by('id')
    notice = Notice.objects.latest('id')
    context = {'teacher': teacher, 'teacher_table': teacher_table, 'notice': notice}
    return render(request, 'reserve/reserve_main.html', context)

@login_required(login_url='common:login')
def detail(request, teacher_id):
    today = date.today()
    current_teacher_id = int(teacher_id)
    teacher_table = Teacher.objects.order_by('id')
    teacher = Teacher.objects.get(id=teacher_id)
    reserve = Reserve.objects.order_by('id')
    context = {'teacher': teacher, 'teacher_table': teacher_table, 'reserve': reserve, 'today': today, 'current_teacher_id': current_teacher_id}
    return render(request, 'reserve/reserve_detail.html', context)