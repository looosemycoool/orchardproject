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
    attendance = get_object_or_404(Attendance, id=attendance_id)

    attendance.morning_check = 'morning_check_{}'.format(attendance_id) in request.POST
    attendance.lunch_check = 'lunch_check_{}'.format(attendance_id) in request.POST
    attendance.night_check = 'night_check_{}'.format(attendance_id) in request.POST
    attendance.absent = 'absent_{}'.format(attendance_id) in request.POST
    attendance.memo = request.POST.get('memo_{}'.format(attendance_id), '')

    morning_late_value = request.POST.get(f'morning_late_{attendance_id}', '').strip()
    lunch_late_value = request.POST.get(f'lunch_late_{attendance_id}', '').strip()
    night_late_value = request.POST.get(f'night_late_{attendance_id}', '').strip()
    early_leave_value = request.POST.get(f'early_leave_{attendance_id}', '').strip()

    attendance.morning_late = morning_late_value if morning_late_value else None
    attendance.lunch_late = lunch_late_value if lunch_late_value else None
    attendance.night_late = night_late_value if night_late_value else None
    attendance.early_leave = early_leave_value if early_leave_value else None

    attendance.time8_check = 'time8_check_{}'.format(attendance_id) in request.POST
    attendance.time9_check = 'time9_check_{}'.format(attendance_id) in request.POST
    attendance.time10_check = 'time10_check_{}'.format(attendance_id) in request.POST
    attendance.time11_check = 'time11_check_{}'.format(attendance_id) in request.POST
    attendance.time12_check = 'time12_check_{}'.format(attendance_id) in request.POST
    attendance.time13_check = 'time13_check_{}'.format(attendance_id) in request.POST
    attendance.time14_check = 'time14_check_{}'.format(attendance_id) in request.POST
    attendance.time15_check = 'time15_check_{}'.format(attendance_id) in request.POST
    attendance.time16_check = 'time16_check_{}'.format(attendance_id) in request.POST
    attendance.time17_check = 'time17_check_{}'.format(attendance_id) in request.POST
    attendance.time18_check = 'time18_check_{}'.format(attendance_id) in request.POST
    attendance.time19_check = 'time19_check_{}'.format(attendance_id) in request.POST
    attendance.time20_check = 'time20_check_{}'.format(attendance_id) in request.POST
    attendance.time21_check = 'time21_check_{}'.format(attendance_id) in request.POST
    attendance.time22_check = 'time22_check_{}'.format(attendance_id) in request.POST

    attendance.save()

    # Redirect back to the attendance page to see the updated records
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