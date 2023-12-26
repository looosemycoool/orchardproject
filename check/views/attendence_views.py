from django.shortcuts import render, redirect
from datetime import datetime
from ..models import Attendance, StudentRegister
from ..forms import AttendanceForm

def attendance_p(request):
    current_date = datetime.now().date()
    attendances_p = Attendance.objects.filter(user__class_name='P', date=current_date).order_by('user__class_num')

    if request.method == 'POST':
        for attendance in attendances_p:
            form = AttendanceForm(request.POST, instance=attendance)
            if form.is_valid():
                form.save()
                return redirect('check:attendance_p')

    translation_dict = {
        'False': '',
        'korean': '국어',
        'math': '수학',
        'english': '영어',
        'research': '탐구',
        'guitar': '기타',
    }

    # attendances_s의 값 변환
    for attendance in attendances_p:
        for field in ['time8', 'time9', 'time10', 'time11', 'time12', 'time13', 'time14', 'time15', 'time16', 'time17',
                      'time18', 'time19', 'time20', 'time21', 'time22']:
            setattr(attendance, field, translation_dict.get(getattr(attendance, field), getattr(attendance, field)))

    context = {'attendances_p': attendances_p}
    return render(request, 'check/attendance_p_class.html', context)

def attendance_s(request):
    current_date = datetime.now().date()
    attendances_s = Attendance.objects.filter(user__class_name='S', date=current_date).order_by('user__class_num')

    # 딕셔너리 정의: CHOICES에 맞게 값 변환
    translation_dict = {
        'False': ' ',
        'korean': '국어',
        'math': '수학',
        'english': '영어',
        'research': '탐구',
        'guitar': '기타',
    }

    # attendances_s의 값 변환
    for attendance in attendances_s:
        for field in ['time8', 'time9', 'time10', 'time11', 'time12', 'time13', 'time14', 'time15', 'time16', 'time17',
                      'time18', 'time19', 'time20', 'time21', 'time22']:
            setattr(attendance, field, translation_dict.get(getattr(attendance, field), getattr(attendance, field)))

    context = {'attendances_s': attendances_s}
    return render(request, 'check/attendance_s_class.html', context)
