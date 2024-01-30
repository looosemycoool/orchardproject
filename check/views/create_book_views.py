from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
from ..models import Attendance, StudentRegister, PatrolCheck
from django.contrib import messages

def get_day_of_week(selected_date):
    date_object = datetime.strptime(selected_date, "%Y-%m-%d").date()
    return date_object.strftime("%a")

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def create_book(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date', None)
        day_of_week = get_day_of_week(selected_date)

        # 8부터 22까지의 시간대에 해당하는 필드가 비어 있지 않은 경우를 확인
        time_fields = [f"{day_of_week.lower()}{hour}" for hour in range(8, 23)]
        filter_params = {f"{field}__isnull": False for field in time_fields}

        students = StudentRegister.objects.filter(**filter_params, is_dropped=False)

        for student in students:
            if not Attendance.objects.filter(user=student, date=selected_date).exists():
                create_attendance(request, student.id, selected_date)

        messages.success(request, f'{selected_date} 출석부가 성공적으로 생성되었습니다.')
        return redirect('check:index')

    return render(request, 'check/check_main.html')

def create_attendance(request, student_register_id, selected_date):
    # student_register_id를 기반으로 해당하는 StudentRegister 모델 인스턴스 가져오기
    student_register = StudentRegister.objects.get(pk=student_register_id)

    # 선택된 날짜로부터 요일을 구함 (월요일: 0, 일요일: 6)
    day_of_week = datetime.strptime(selected_date, '%Y-%m-%d').weekday()

    # 요일에 따라 StudentRegister 모델의 필드와 Attendance 모델의 필드를 동적으로 매핑
    day_mapping = {
        0: 'mon',
        1: 'tue',
        2: 'wed',
        3: 'thu',
        4: 'fri',
        5: 'sat',
        6: 'sun',
    }
    attendance_instance = Attendance(user=student_register, date=selected_date)
    # 시간대에 해당하는 필드를 연결
    for hour in range(8, 23):  # 8부터 22까지 반복
        time_attribute_name = f"{day_mapping[day_of_week]}{hour}"
        # Attendance 모델 인스턴스 생성

        # 해당하는 시간대의 값을 가져와서 Attendance 모델과 연결
        time_value = getattr(student_register, time_attribute_name)
        setattr(attendance_instance, f"time{hour}", time_value)

        # Attendance 모델 인스턴스 저장
        attendance_instance.save()

    # 이후 필요한 작업 수행 (예: 리다이렉트 등)
    return render(request, 'check/check_main.html')

def create_patrol_book(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date', None)
        day_of_week = get_day_of_week(selected_date)

        # 8부터 22까지의 시간대에 해당하는 필드가 비어 있지 않은 경우를 확인
        time_fields = [f"{day_of_week.lower()}{hour}" for hour in range(8, 23)]
        filter_params = {f"{field}__isnull": False for field in time_fields}

        students = StudentRegister.objects.filter(**filter_params, is_dropped=False)

        for student in students:
            if not PatrolCheck.objects.filter(user=student, date=selected_date).exists():
                create_patrol(request, student.id, selected_date)

        messages.success(request, f'{selected_date} 일일 순찰이 성공적으로 생성되었습니다.')
        return redirect('check:index')

    return render(request, 'check/check_main.html')

def create_patrol(request, student_register_id, selected_date):
    student_register = StudentRegister.objects.get(pk=student_register_id)
    day_of_week = datetime.strptime(selected_date, '%Y-%m-%d').strftime('%a').lower()

    patrol_check_instance = PatrolCheck(user=student_register, date=selected_date, day_of_week=day_of_week)
    patrol_check_instance.save()

    return render(request, 'check/check_main.html')

