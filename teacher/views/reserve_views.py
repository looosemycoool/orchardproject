from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from reserve.models import Reserve, Teacher, Notice

@user_passes_test(lambda u: u.is_staff, login_url="common:login")
def reserve_history(request, teacher_id):
    current_teacher_id = int(teacher_id)
    teacher_table = Teacher.objects.order_by('id')

    dates = Reserve.objects.filter(teacher_id=current_teacher_id).values_list('date', flat=True).distinct().order_by(
        '-date')

    context = {
        'teacher_table': teacher_table,
        'current_teacher_id': current_teacher_id,
        'dates': dates,
    }
    return render(request, 'teacher/reserve/reserve_history.html', context)

@login_required(login_url='common:login')
def reserve_history_detail(request, teacher_id, date):
    current_teacher_id = int(teacher_id)
    teacher_table = Teacher.objects.order_by('id')

    selected_date = date  # 선택한 날짜

    # 해당 선생님의 예약 데이터 중 선택한 날짜에 해당하는 데이터 필터링
    reserve = Reserve.objects.filter(teacher_id=current_teacher_id, date=selected_date).order_by('id')

    dates = Reserve.objects.filter(teacher_id=current_teacher_id).values_list('date', flat=True).distinct().order_by(
        '-date')

    context = {
        'current_teacher_id': current_teacher_id,
        'selected_date': selected_date,
        'reserve': reserve,
        'teacher_table': teacher_table,
        'dates': dates,
    }
    return render(request, 'teacher/reserve/reserve_history_detail.html', context)