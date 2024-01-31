from django.shortcuts import render, redirect
from reserve.models import Teacher, Time_Table, Reserve
from django.urls import reverse
from django.contrib.auth.models import User

def reserve(request):
    teacher_table = Teacher.objects.order_by('id')
    return render(request, 'manager/reserve/manager_reserve_main.html', {'teacher_table': teacher_table})

def reserve_create(request):
    if request.method == 'POST':
        teacher_table = Teacher.objects.order_by('id')
        teacher_id = request.POST.get('teacher_name')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        teacher_name = Teacher.objects.get(id=teacher_id)
        start_time_obj = Time_Table.objects.get(time=start_time)
        end_time_obj = Time_Table.objects.get(time=end_time)

        reserve_data = []

        for i in range(start_time_obj.id, end_time_obj.id + 1, 2):
            reserve = Reserve(
                date=date,
                teacher_id=teacher_name,
                time=Time_Table.objects.get(id=i),
            )
            reserve.save()
            reserve_data.append(reserve)

        success_message = "예약이 생성되었습니다."

        context = {
            'teacher_name': teacher_name,
            'date': date,
            'reserve_data': reserve_data,
            'success_message': success_message,
            'teacher_table': teacher_table,
        }
        return render(request, 'manager/reserve/manager_reserve_create.html', context)
    else:
        # 모델에 필요한 데이터 조회 및 전달
        teachers = Teacher.objects.all()
        time_table = Time_Table.objects.all()
        teacher_table = Teacher.objects.filter(retired=False).order_by('id')

        context = {
            'teachers': teachers,
            'time_table': time_table,
            'teacher_table': teacher_table,
        }
        return render(request, 'manager/reserve/manager_reserve_create.html', context)


def reserve_detail(request, teacher_id):
    current_teacher_id = int(teacher_id)
    teacher_table = Teacher.objects.order_by('id')

    dates = Reserve.objects.filter(teacher_id=current_teacher_id).values_list('date', flat=True).distinct().order_by(
        '-date')

    context = {
        'current_teacher_id': current_teacher_id,
        'reserve': reserve,
        'teacher_table': teacher_table,
        'dates': dates,
    }
    return render(request, 'manager/reserve/manager_reserve_detail.html', context)

def reserve_detail_teacher(request, teacher_id, date):
    current_teacher_id = int(teacher_id)
    teacher_table = Teacher.objects.order_by('id')
    selected_date = date  # 선택한 날짜
    # 해당 선생님의 예약 데이터 중 선택한 날짜에 해당하는 데이터 필터링
    reserve_filter_teacher = Reserve.objects.filter(teacher_id=current_teacher_id, date=selected_date).order_by('id')

    dates = Reserve.objects.filter(teacher_id=current_teacher_id).values_list('date', flat=True).distinct().order_by(
        '-date')

    students = User.objects.filter(is_staff=False).values('first_name').order_by('first_name')

    context = {
        'current_teacher_id': current_teacher_id,
        'selected_date': selected_date,
        'reserve_filter_teacher': reserve_filter_teacher,
        'teacher_table': teacher_table,
        'dates': dates,
        'students': students
    }
    return render(request, 'manager/reserve/manager_reserve_detail.html', context)

def reserve_update(request, reserve_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        reserve = Reserve.objects.get(id=reserve_id)

        if action == '상담':
            student_name = request.POST.get('student_name')
            student = User.objects.get(first_name=student_name)
            reserve.student_name = student
            reserve.save()

        elif action == '초기화':
            reserve.student_name = None
            reserve.save()
            # 예약 상태 변경 후 리다이렉트 등의 동작 수행
        elif action == '삭제':
            reserve.delete()
    return redirect(reverse('manager:reserve_detail_teacher', kwargs={'teacher_id': reserve.teacher_id.id, 'date': reserve.date}))
