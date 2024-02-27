from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ..models import Student_Study_Data, WeekPlan
from check.models import StudentRegister
from ..forms import Student_Study_DataForm, WeekPlanForm
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
    data = WeekPlan.objects.filter(user__id=student_id).order_by('-id')
    student = StudentRegister.objects.filter(id=student_id) # 단일 객체를 가져오기

    selected_week = request.GET.get('selected_week')

    if selected_week:
        filtered_data = WeekPlan.objects.filter(week_name=selected_week, user__id=student_id)
        week_total_korean_lecture_study = (filtered_data[0].mon_korean_lecture_study_hour * 60) + filtered_data[0].mon_korean_lecture_study_min + (filtered_data[0].tue_korean_lecture_study_hour * 60) + filtered_data[0].tue_korean_lecture_study_min + (filtered_data[0].wed_korean_lecture_study_hour * 60) + filtered_data[0].wed_korean_lecture_study_min + (filtered_data[0].thu_korean_lecture_study_hour * 60) + filtered_data[0].thu_korean_lecture_study_min + (filtered_data[0].fri_korean_lecture_study_hour * 60) + filtered_data[0].fri_korean_lecture_study_min + (filtered_data[0].sat_korean_lecture_study_hour * 60) + filtered_data[0].sat_korean_lecture_study_min + (filtered_data[0].sun_korean_lecture_study_hour * 60) + filtered_data[0].sun_korean_lecture_study_min
        week_total_korean_self_study = (filtered_data[0].mon_korean_self_study_hour * 60) + filtered_data[0].mon_korean_self_study_min + (filtered_data[0].tue_korean_self_study_hour * 60) + filtered_data[0].tue_korean_self_study_min + (filtered_data[0].wed_korean_self_study_hour * 60) + filtered_data[0].wed_korean_self_study_min + (filtered_data[0].thu_korean_self_study_hour * 60) + filtered_data[0].thu_korean_self_study_min + (filtered_data[0].fri_korean_self_study_hour * 60) + filtered_data[0].fri_korean_self_study_min + (filtered_data[0].sat_korean_self_study_hour * 60) + filtered_data[0].sat_korean_self_study_min + (filtered_data[0].sun_korean_self_study_hour * 60) + filtered_data[0].sun_korean_self_study_min
        week_total_math_lecture_study = (filtered_data[0].mon_math_lecture_study_hour * 60) + filtered_data[0].mon_math_lecture_study_min + (filtered_data[0].tue_math_lecture_study_hour * 60) + filtered_data[0].tue_math_lecture_study_min + (filtered_data[0].wed_math_lecture_study_hour * 60) + filtered_data[0].wed_math_lecture_study_min + (filtered_data[0].thu_math_lecture_study_hour * 60) + filtered_data[0].thu_math_lecture_study_min + (filtered_data[0].fri_math_lecture_study_hour * 60) + filtered_data[0].fri_math_lecture_study_min + (filtered_data[0].sat_math_lecture_study_hour * 60) + filtered_data[0].sat_math_lecture_study_min + (filtered_data[0].sun_math_lecture_study_hour * 60) + filtered_data[0].sun_math_lecture_study_min
        week_total_math_self_study = (filtered_data[0].mon_math_self_study_hour * 60) + filtered_data[0].mon_math_self_study_min + (filtered_data[0].tue_math_self_study_hour * 60) + filtered_data[0].tue_math_self_study_min + (filtered_data[0].wed_math_self_study_hour * 60) + filtered_data[0].wed_math_self_study_min + (filtered_data[0].thu_math_self_study_hour * 60) + filtered_data[0].thu_math_self_study_min + (filtered_data[0].fri_math_self_study_hour * 60) + filtered_data[0].fri_math_self_study_min + (filtered_data[0].sat_math_self_study_hour * 60) + filtered_data[0].sat_math_self_study_min + (filtered_data[0].sun_math_self_study_hour * 60) + filtered_data[0].sun_math_self_study_min

        week_total_english_lecture_study = (filtered_data[0].mon_english_lecture_study_hour * 60) + filtered_data[
            0].mon_english_lecture_study_min + (filtered_data[0].tue_english_lecture_study_hour * 60) + filtered_data[
                                            0].tue_english_lecture_study_min + (
                                                    filtered_data[0].wed_english_lecture_study_hour * 60) + filtered_data[
                                            0].wed_english_lecture_study_min + (
                                                    filtered_data[0].thu_english_lecture_study_hour * 60) + filtered_data[
                                            0].thu_english_lecture_study_min + (
                                                    filtered_data[0].fri_english_lecture_study_hour * 60) + filtered_data[
                                            0].fri_english_lecture_study_min + (
                                                    filtered_data[0].sat_english_lecture_study_hour * 60) + filtered_data[
                                            0].sat_english_lecture_study_min + (
                                                    filtered_data[0].sun_english_lecture_study_hour * 60) + filtered_data[
                                            0].sun_english_lecture_study_min
        week_total_english_self_study = (filtered_data[0].mon_english_self_study_hour * 60) + filtered_data[
            0].mon_math_self_study_min + (filtered_data[0].tue_english_self_study_hour * 60) + filtered_data[
                                         0].tue_english_self_study_min + (filtered_data[0].wed_english_self_study_hour * 60) + \
                                     filtered_data[0].wed_english_self_study_min + (
                                                 filtered_data[0].thu_english_self_study_hour * 60) + filtered_data[
                                         0].thu_english_self_study_min + (filtered_data[0].fri_english_self_study_hour * 60) + \
                                     filtered_data[0].fri_english_self_study_min + (
                                                 filtered_data[0].sat_english_self_study_hour * 60) + filtered_data[
                                         0].sat_english_self_study_min + (filtered_data[0].sun_english_self_study_hour * 60) + \
                                     filtered_data[0].sun_english_self_study_min

        week_total_research_lecture_study = (filtered_data[0].mon_research_lecture_study_hour * 60) + filtered_data[
            0].mon_english_lecture_study_min + (filtered_data[0].tue_research_lecture_study_hour * 60) + filtered_data[
                                               0].tue_research_lecture_study_min + (
                                                   filtered_data[0].wed_research_lecture_study_hour * 60) + \
                                           filtered_data[
                                               0].wed_research_lecture_study_min + (
                                                   filtered_data[0].thu_research_lecture_study_hour * 60) + \
                                           filtered_data[
                                               0].thu_research_lecture_study_min + (
                                                   filtered_data[0].fri_research_lecture_study_hour * 60) + \
                                           filtered_data[
                                               0].fri_research_lecture_study_min + (
                                                   filtered_data[0].sat_research_lecture_study_hour * 60) + \
                                           filtered_data[
                                               0].sat_research_lecture_study_min + (
                                                   filtered_data[0].sun_research_lecture_study_hour * 60) + \
                                           filtered_data[
                                               0].sun_research_lecture_study_min
        week_total_research_self_study = (filtered_data[0].mon_research_self_study_hour * 60) + filtered_data[
            0].mon_research_self_study_min + (filtered_data[0].tue_research_self_study_hour * 60) + filtered_data[
                                            0].tue_research_self_study_min + (
                                                    filtered_data[0].wed_research_self_study_hour * 60) + \
                                        filtered_data[0].wed_research_self_study_min + (
                                                filtered_data[0].thu_research_self_study_hour * 60) + filtered_data[
                                            0].thu_research_self_study_min + (
                                                    filtered_data[0].fri_research_self_study_hour * 60) + \
                                        filtered_data[0].fri_research_self_study_min + (
                                                filtered_data[0].sat_research_self_study_hour * 60) + filtered_data[
                                            0].sat_research_self_study_min + (
                                                    filtered_data[0].sun_research_self_study_hour * 60) + \
                                        filtered_data[0].sun_research_self_study_min

        week_total_lecture_study = week_total_korean_lecture_study + week_total_math_lecture_study + week_total_english_lecture_study + week_total_research_lecture_study
        week_total_self_study = week_total_korean_self_study + week_total_math_self_study + week_total_english_self_study + week_total_research_self_study
    else:
        filtered_data = []
        week_total_korean_lecture_study = 0
        week_total_math_lecture_study = 0
        week_total_english_lecture_study = 0
        week_total_research_lecture_study = 0

        week_total_korean_self_study = 0
        week_total_math_self_study = 0
        week_total_english_self_study = 0
        week_total_research_self_study = 0
        week_total_lecture_study = 0
        week_total_self_study = 0

    print(student)
    context = {
        'data': data,
        'student': student,
        'selected_week': selected_week,
        'filtered_data': filtered_data,
        'week_total_korean_lecture_study': week_total_korean_lecture_study,
        'week_total_math_lecture_study': week_total_math_lecture_study,
        'week_total_english_lecture_study': week_total_english_lecture_study,
        'week_total_research_lecture_study': week_total_research_lecture_study,
        'week_total_korean_self_study': week_total_korean_self_study,
        'week_total_math_self_study': week_total_math_self_study,
        'week_total_english_self_study': week_total_english_self_study,
        'week_total_research_self_study': week_total_research_self_study,
        'week_total_lecture_study': week_total_lecture_study,
        'week_total_self_study': week_total_self_study,
    }
    return render(request, 'manager/weekplan/weekplan_detail.html', context)

def weekplan_create(request, student_id):
    student = StudentRegister.objects.get(id=student_id)  # 단일 객체 가져오기
    data = WeekPlan.objects.filter(user__id=student_id).order_by('-id')

    if request.method == 'POST':
        form = WeekPlanForm(request.POST)
        if form.is_valid():
            week_name = form.cleaned_data['week_name']
            # 중복 검사
            if WeekPlan.objects.filter(user=student, week_name=week_name).exists():
                form.add_error('week_name', ValidationError(_("이미 등록된 기간입니다.")))
                context = {'student': student, 'form': form, 'data': data}
                return render(request, 'manager/weekplan/weekplan_form.html', context)

            weekplan = form.save(commit=False)
            weekplan.user = StudentRegister.objects.get(id=student_id)
            student_id = student.id
            weekplan.save()
            return redirect('manager:weekplan_detail', student_id=student_id)
    else:
        form = WeekPlanForm()

    context = {'student': student, 'form': form, 'data': data}
    return render(request, 'manager/weekplan/weekplan_form.html', context)

def weekplan_modify(request, data_id):
    week_data = get_object_or_404(WeekPlan, id=data_id)  # 단일 객체 가져오기
    data = WeekPlan.objects.filter(user__id=week_data.user_id).order_by('-id')

    student = get_object_or_404(StudentRegister, id=week_data.user_id)
    student_id = student.id

    if request.method == 'POST':
        form = WeekPlanForm(request.POST, instance=week_data)
        if form.is_valid():
            study_data = form.save(commit=False)
            study_data.user = StudentRegister.objects.get(id=student_id)  # StudentRegister 인스턴스를 할당
            study_data.save()
            return redirect('manager:weekplan_detail', student_id=student_id)

    else:
        form = WeekPlanForm(instance=week_data)

    context = {'form': form, 'data': data, 'student': student, 'week_data': week_data}
    return render(request, 'manager/weekplan/weekplan_form.html', context)

def weekplan_delete(request, data_id):
    week_data = get_object_or_404(WeekPlan, id=data_id)
    student_id = week_data.user_id
    week_data.delete()
    return redirect('manager:weekplan_detail', student_id=student_id)
