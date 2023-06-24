from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from reserve.models import Reserve, Teacher, Notice
from django.contrib import messages

from .models import Consulting
from .forms import ConsultingForm

from datetime import date
from django.core.paginator import Paginator

@login_required(login_url='common:login')
@user_passes_test(lambda u: u.is_staff, login_url="common:login")
def index(request):
    teacher_table = Teacher.objects.order_by('id')
    return render(request, 'teacher/reserve/reserve_main.html', {'teacher_table': teacher_table})

## 새 코드
@user_passes_test(lambda u: u.is_staff, login_url="common:login")
def reserve_history(request, teacher_id):
    current_teacher_id = int(teacher_id)
    teacher_table = Teacher.objects.order_by('id')

    dates = Reserve.objects.filter(teacher_id=current_teacher_id).values_list('date', flat=True).distinct().order_by(
        '-date')

    messages.error(request, '권한이 없습니다.')

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


@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def consulting_page(request):
    consulting = Consulting.objects.order_by('-id')
    teacher = Teacher.objects.order_by('id')

    page = request.GET.get('page', '1')
    paginator = Paginator(consulting, 15)
    page_obj = paginator.get_page(page)

    context = {'teacher': teacher, 'consulting': page_obj}
    return render(request, 'teacher/consulting/consulting_main.html', context)

@login_required(login_url='common:login')
def consulting_detail(request, consulting_id):
	consulting = Consulting.objects.get(id=consulting_id)
	context = {'consulting': consulting}
	return render(request, 'teacher/consulting/consulting_detail.html', context)


@login_required(login_url='common:login')
def consulting_create(request):
    if request.method == 'POST':
        form = ConsultingForm(request.POST)
        if form.is_valid():
            consulting = form.save(commit=False)
            consulting.teacher_name = request.user
            consulting_type = form.cleaned_data.get('consulting_type')
            if consulting_type == 'other':
                other_consulting_type = form.cleaned_data.get('other_consulting_type')
                consulting.consulting_type = other_consulting_type
            else:
                consulting.consulting_type = consulting_type
            consulting.save()
            return redirect('teacher:index')
    else:
        form = ConsultingForm()
    context = {'form': form}
    return render(request, 'teacher/consulting/consulting_form.html', context)