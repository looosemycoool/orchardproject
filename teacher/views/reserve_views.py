from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from reserve.models import Reserve, Teacher, Notice
from reserve.models import Reserve
from reserve.forms import ConsultForm

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

def consult_create(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            reserve.type = form.cleaned_data.get('type')
            reserve.subject = form.cleaned_data['subject']
            reserve.content = form.cleaned_data['content']
            reserve.title = form.cleaned_data['title']
            reserve.save()
            teacher_id = reserve.teacher_id.id
            return redirect('teacher:reserve_history_detail', teacher_id=teacher_id, date=reserve.date)
    else:
        form = ConsultForm()

    return render(request, 'teacher/reserve/reserve_history_form.html', {'form': form, 'reserve': reserve})

def consult_modify(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    if request.method == 'POST':
        form = ConsultForm(request.POST, instance=reserve)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.save()
            teacher_id = reserve.teacher_id.id
            return redirect('teacher:reserve_history_detail', teacher_id=teacher_id, date=reserve.date)
    else:
        form = ConsultForm(instance=reserve)

    return render(request, 'teacher/reserve/reserve_history_form.html', {'form': form, 'reserve': reserve})