from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from ..forms import AttendanceForm
from ..models import Attendance


@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def index(request):
    attendances = None
    selected_date = None
    selected_class = None

    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        selected_class = request.POST.get('class_button')  # 'P' 또는 'S'

        if selected_date and selected_class:
            attendances = Attendance.objects.filter(date=selected_date, user__class_name=selected_class).order_by('user__class_num')

            # 드롭다운 메뉴에서 선택된 값들을 처리
            for attendance in attendances:
                for time_slot in range(8, 23):  # 시간대별 필드 (예: time8, time9, ..., time22)
                    time_field = f"time{time_slot}"
                    selected_value = request.POST.get(f"{time_field}_{attendance.id}")
                    if selected_value is not None:
                        setattr(attendance, time_field, selected_value)
                attendance.save()

    context = {
        'attendances': attendances,
        'selected_date': selected_date,
        'selected_class': selected_class
    }
    return render(request, 'check/check_main.html', context)

def update_attendance(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('check:index')

# def update_
