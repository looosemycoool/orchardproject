from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ..models import Student_Study_Data, Average_Study_Data
from check.models import StudentRegister
from ..forms import Student_Study_DataForm
from django.conf import settings
from collections import defaultdict

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def weekplan(request):
    students_p = StudentRegister.objects.filter(class_name='P', is_dropped=False).order_by('class_num')
    students_s = StudentRegister.objects.filter(class_name='S', is_dropped=False).order_by('class_num')
    students_m = StudentRegister.objects.filter(class_name='M', is_dropped=False).order_by('class_num')

    p_line1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
    p_line2 = ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    s_line1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
               '18', '19', '20']
    s_line2 = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
               '38', '39', '40']
    s_line3 = ['41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57',
               '58', '59', '60']

    context = {'students_p': students_p, 'students_s': students_s, 'students_m': students_m, 'p_line1': p_line1,
               'p_line2': p_line2, 's_line1': s_line1, 's_line2': s_line2, 's_line3': s_line3}
    return render(request, 'manager/weekplan/weekplan_main.html', context)

def weekplan_detail(request, student_id):
    data = Student_Study_Data.objects.filter(user__id=student_id).order_by('-id')
    student = StudentRegister.objects.filter(id=student_id) # 단일 객체를 가져오기
    research1 = student.values('research1_select')[0]['research1_select']
    research2 = student.values('research2_select')[0]['research2_select']
    # research3 = student.values('research3_select')[0]['research3_select']

    selected_week = request.GET.get('selected_week')

    if selected_week:
        filtered_data = Student_Study_Data.objects.filter(week_name=selected_week, user__id=student_id)
        total_study = filtered_data[0].korean_study + filtered_data[0].math_study + filtered_data[0].english_study + filtered_data[0].research1_study + filtered_data[0].research2_study
        total_self_study = filtered_data[0].korean_self_study + filtered_data[0].math_self_study + filtered_data[0].english_self_study + filtered_data[0].research1_self_study + filtered_data[0].research2_self_study
    else:
        filtered_data = []
        total_study = 0
        total_self_study = 0

    print(student)
    context = {
        'data': data,
        'student': student,
        'research1': research1,
        'research2': research2,
        'selected_week': selected_week,
        'filtered_data': filtered_data,
        'total_study': total_study,
        'total_self_study': total_self_study
    }
    return render(request, 'manager/weekplan/weekplan_detail.html', context)

def weekplan_create(request, student_id):
    student = StudentRegister.objects.get(id=student_id)  # 단일 객체 가져오기
    data = Student_Study_Data.objects.filter(user__id=student_id).order_by('-id')

    if request.method == 'POST':
        form = Student_Study_DataForm(request.POST)
        if form.is_valid():
            week_name = form.cleaned_data['week_name']
            # 중복 검사
            if Student_Study_Data.objects.filter(user=student, week_name=week_name).exists():
                form.add_error('week_name', ValidationError(_("이미 등록된 기간입니다.")))
                context = {'student': student, 'form': form, 'data': data}
                return render(request, 'manager/weekplan/weekplan_form.html', context)

            study_data = form.save(commit=False)
            study_data.week_name = form.cleaned_data['week_name']
            # study_data.student_name = student
            study_data.user = student
            study_data.korean_study = form.cleaned_data['korean_study']
            study_data.korean_self_study = form.cleaned_data['korean_self_study']

            study_data.math_study = form.cleaned_data['math_study']
            study_data.math_self_study = form.cleaned_data['math_self_study']

            study_data.english_study = form.cleaned_data['english_study']
            study_data.english_self_study = form.cleaned_data['english_self_study']

            study_data.research1_study = form.cleaned_data['research1_study']
            study_data.research1_self_study = form.cleaned_data['research1_self_study']

            # study_data.research2_study = form.cleaned_data['research2_study']
            # study_data.research2_self_study = form.cleaned_data['research2_self_study']
            #
            # study_data.research3_study = form.cleaned_data['research3_study']
            # study_data.research3_self_study = form.cleaned_data['research3_self_study']
            study_data.save()  # 데이터 저장
            student_id = student.id
            return redirect('manager:weekplan_detail', student_id=student_id)
    else:
        form = Student_Study_DataForm()

    context = {'student': student, 'form': form, 'data': data}
    return render(request, 'manager/weekplan/weekplan_form.html', context)

def weekplan_modify(request, data_id):
    week_data = get_object_or_404(Student_Study_Data, id=data_id)  # 단일 객체 가져오기
    data = Student_Study_Data.objects.filter(user__id=week_data.user_id).order_by('-id')

    student = get_object_or_404(StudentRegister, id=week_data.user_id)
    student_id = student.id

    if request.method == 'POST':
        form = Student_Study_DataForm(request.POST, instance=week_data)
        # if form.is_valid():
        #     study_data = form.save(commit=False)
        #     study_data.user = student.id
        #     # 필요한 경우 study_data의 추가 필드를 업데이트
        #     study_data.save()  # 데이터 저장
        #     student_id = student.id
        #     return redirect('manager:student_study_detail', student_id=student_id)
        if form.is_valid():
            study_data = form.save(commit=False)
            # student_id = form.cleaned_data.get('user')  # 또는 week_data.user_id 등을 사용
            study_data.user = StudentRegister.objects.get(id=student_id)  # StudentRegister 인스턴스를 할당
            # study_data.student_name = week_data.student_name
            study_data.save()
            return redirect('manager:weekplan_detail', student_id=student_id)

    else:
        form = Student_Study_DataForm(instance=week_data)

    context = {'form': form, 'data': data, 'student': student, 'week_data': week_data}
    return render(request, 'manager/weekplan/weekplan_form.html', context)

def weekplan_delete(request, data_id):
    week_data = get_object_or_404(Student_Study_Data, id=data_id)
    student_id = week_data.user_id
    week_data.delete()
    return redirect('manager:weekplan_detail', student_id=student_id)
