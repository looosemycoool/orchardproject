from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect

from ..forms import AttendanceForm
from ..models import Attendance, Specify

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def index(request):
    content_instance, created = Specify.objects.get_or_create(pk=1)
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')

        return redirect('check:detail',  selected_date)

    return render(request, 'check/check_main.html', {'content': content_instance.content})

# def detail(request, selected_class, selected_date):
#     if selected_date and selected_class:
#         attendances = Attendance.objects.filter(date=selected_date, user__class_name=selected_class).order_by('user__class_num')
#
#         for attendance in attendances:
#             for time_slot in range(8, 23):
#                 time_field = f"time{time_slot}"
#                 selected_value = request.POST.get(f"{time_field}_{attendance.id}")
#                 if selected_value is not None:
#                     setattr(attendance, time_field, selected_value)
#             attendance.save()
#         translation_dict = {
#             'False': ' ',
#             'korean': '국어',
#             'math': '수학',
#             'english': '영어',
#             'research': '탐구',
#             'guitar': '기타',
#             'specify': '특이',
#         }
#         # attendances_s의 값 변환
#         for attendance in attendances:
#             for field in ['time8', 'time9', 'time10', 'time11', 'time12', 'time13', 'time14', 'time15', 'time16',
#                           'time17', 'time18', 'time19', 'time20', 'time21', 'time22']:
#                 setattr(attendance, field, translation_dict.get(getattr(attendance, field), getattr(attendance, field)))
#
#     context = {
#         'attendances': attendances,
#         'selected_date': selected_date,
#         'selected_class': selected_class
#     }
#     return render(request, 'check/check_search.html', context)

def detail(request, selected_date):
    if selected_date:
        attendances_p = Attendance.objects.filter(date=selected_date, user__class_name='P').order_by('user__class_num')
        attendances_s = Attendance.objects.filter(date=selected_date, user__class_name='S').order_by('user__class_num')
        attendances_m = Attendance.objects.filter(date=selected_date, user__class_name='M').order_by('user__class_num')

        for attendance in attendances_p:
            for time_slot in range(8, 23):
                time_field = f"time{time_slot}"
                selected_value = request.POST.get(f"{time_field}_{attendance.id}")
                if selected_value is not None:
                    setattr(attendance, time_field, selected_value)
            attendance.save()

        for attendance in attendances_s:
            for time_slot in range(8, 23):
                time_field = f"time{time_slot}"
                selected_value = request.POST.get(f"{time_field}_{attendance.id}")
                if selected_value is not None:
                    setattr(attendance, time_field, selected_value)
            attendance.save()

        for attendance in attendances_m:
            for time_slot in range(8, 23):
                time_field = f"time{time_slot}"
                selected_value = request.POST.get(f"{time_field}_{attendance.id}")
                if selected_value is not None:
                    setattr(attendance, time_field, selected_value)
            attendance.save()

        translation_dict = {
            'False': ' ',
            'korean': '국어',
            'math': '수학',
            'english': '영어',
            'research': '탐구',
            'guitar': '기타',
            'specify': '특이',
        }

        for attendance in attendances_p:
            for field in ['time8', 'time9', 'time10', 'time11', 'time12', 'time13', 'time14', 'time15', 'time16',
                          'time17', 'time18', 'time19', 'time20', 'time21', 'time22']:
                setattr(attendance, field, translation_dict.get(getattr(attendance, field), getattr(attendance, field)))

        for attendance in attendances_s:
            for field in ['time8', 'time9', 'time10', 'time11', 'time12', 'time13', 'time14', 'time15', 'time16',
                          'time17', 'time18', 'time19', 'time20', 'time21', 'time22']:
                setattr(attendance, field, translation_dict.get(getattr(attendance, field), getattr(attendance, field)))

        for attendance in attendances_m:
            for field in ['time8', 'time9', 'time10', 'time11', 'time12', 'time13', 'time14', 'time15', 'time16',
                          'time17', 'time18', 'time19', 'time20', 'time21', 'time22']:
                setattr(attendance, field, translation_dict.get(getattr(attendance, field), getattr(attendance, field)))

    context = {
        'attendances_p': attendances_p,
        'attendances_s': attendances_s,
        'attendances_m': attendances_m,
        'selected_date': selected_date,
    }
    return render(request, 'check/check_search.html', context)


def update_attendance(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('check:detail', attendance.date)

def specify(request):
    # 데이터베이스에서 Specify 인스턴스를 가져오거나, 없으면 생성합니다.
    content_instance, created = Specify.objects.get_or_create(pk=1)

    if request.method == 'POST':
        # POST 요청으로 데이터를 업데이트합니다.
        content_instance.content = request.POST.get('content', '')
        content_instance.save()
        return redirect('check:index')

    # GET 요청 시, 현재 데이터를 템플릿에 전달합니다.
    return render(request, 'check/check_main.html', {'content': content_instance.content})