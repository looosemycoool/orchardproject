from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime
from ..models import Attendance
from ..forms import AttendanceForm

# CHOICES 정의
CHOICES = {
    'False': '',
    'korean': '국어',
    'math': '수학',
    'english': '영어',
    'research': '탐구',
    'guitar': '기타',
}
@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def attendance_index_p(request):
    current_date = datetime.now().date()
    attendances_p = Attendance.objects.filter(user__class_name='P', date=current_date, user__is_dropped=False).order_by('user__class_num')

    # 각 attendance의 timeXX 필드를 한글로 변환
    for attendance in attendances_p:
        for hour in range(8, 23):  # 8시부터 22시까지
            field_name = f"time{hour}"
            time_value = getattr(attendance, field_name, None)
            if time_value is not None:
                translated_value = CHOICES.get(time_value, time_value)
                setattr(attendance, field_name, translated_value)

    if request.method == 'POST':
        for attendance in attendances_p:
            update_attendance(request, attendance.id)
        return redirect('check:attendance_index_p')

    context = {'attendances_p': attendances_p, 'current_date': current_date}
    return render(request, 'check/attendance/attendance_p_class.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def attendance_index_s(request):
    current_date = datetime.now().date()
    attendances_s = Attendance.objects.filter(user__class_name='S', date=current_date, user__is_dropped=False).order_by('user__class_num')

    # 각 attendance의 timeXX 필드를 한글로 변환
    for attendance in attendances_s:
        for hour in range(8, 23):  # 8시부터 22시까지
            field_name = f"time{hour}"
            time_value = getattr(attendance, field_name, None)
            if time_value is not None:
                translated_value = CHOICES.get(time_value, time_value)
                setattr(attendance, field_name, translated_value)

    if request.method == 'POST':
        for attendance in attendances_s:
            update_attendance(request, attendance.id)
        return redirect('check:attendance_index_s')

    context = {'attendances_s': attendances_s, 'current_date': current_date}
    return render(request, 'check/attendance/attendance_s_class.html', context)

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def attendance_index_m(request):
    current_date = datetime.now().date()
    attendances_m = Attendance.objects.filter(user__class_name='M', date=current_date, user__is_dropped=False).order_by('user__class_num')

    # 각 attendance의 timeXX 필드를 한글로 변환
    for attendance in attendances_m:
        for hour in range(8, 23):  # 8시부터 22시까지
            field_name = f"time{hour}"
            time_value = getattr(attendance, field_name, None)
            if time_value is not None:
                translated_value = CHOICES.get(time_value, time_value)
                setattr(attendance, field_name, translated_value)

    if request.method == 'POST':
        for attendance in attendances_m:
            update_attendance(request, attendance.id)
        return redirect('check:attendance_index_m')

    context = {'attendances_m': attendances_m, 'current_date': current_date}
    return render(request, 'check/attendance/attendance_m_class.html', context)



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
    return redirect('check:index')