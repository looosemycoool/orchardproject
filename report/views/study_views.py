from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from django.conf import settings
from collections import defaultdict

from check.models import StudentRegister, PatrolCheck
from manager.models import Student_Study_Data

def index(request):
    students_p = StudentRegister.objects.filter(class_name='P').order_by('class_num')
    students_s = StudentRegister.objects.filter(class_name='S').order_by('class_num')
    students_m = StudentRegister.objects.filter(class_name='M').order_by('class_num')

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
    return render(request, 'report/study/study_main.html', context)

def study_report(request, student_id):
    study_fields = [
        'time1_study', 'time2_study', 'time3_study', 'time4_study',
        'time5_study', 'time6_study', 'time7_study', 'time8_study',
        'time9_study', 'time10_study', 'time11_study', 'time12_study',
        'time13_study', 'time14_study', 'time15_study', 'time16_study',
        'time17_study', 'time18_study'
    ]
    focus_fields = [
        'time1_focus', 'time2_focus', 'time3_focus', 'time4_focus',
        'time5_focus', 'time6_focus', 'time7_focus', 'time8_focus',
        'time9_focus', 'time10_focus', 'time11_focus', 'time12_focus',
        'time13_focus', 'time14_focus', 'time15_focus', 'time16_focus',
        'time17_focus', 'time18_focus'
    ]

    study_datas = Student_Study_Data.objects.filter(user__id=student_id).order_by('-id')

    weekly_reports = []

    for study in study_datas:
        week_report = {}

        three_count = 0
        two_count = 0
        one_count = 0

        k_ss_count = 0
        k_il_count = 0
        m_ss_count = 0
        m_il_count = 0
        e_ss_count = 0
        e_il_count = 0
        r_ss_count = 0
        r_il_count = 0

        plan = 0
        mentoring = 0
        question = 0
        consulting = 0

        sleep = 0

        print(study.week_name)
        patrol_datas = PatrolCheck.objects.filter(date__gte=study.start_date, date__lte=study.end_date, user__id=student_id)

        for patrol in patrol_datas:
            print(patrol.date)
            for field in study_fields:
                value = getattr(patrol, field)
                if value == 'k_ss':
                    k_ss_count += 1
                elif value == 'k_il':
                    k_il_count += 1
                elif value == 'm_ss':
                    m_ss_count += 1
                elif value == 'm_il':
                    m_il_count += 1
                elif value == 'e_ss':
                    e_ss_count += 1
                elif value == 'e_il':
                    e_il_count += 1
                elif value == 'r_ss':
                    r_ss_count += 1
                elif value == 'r_il':
                    r_il_count += 1
                elif value == 'plan':
                    plan += 1
                elif value == 'mentoring':
                    mentoring += 1
                elif value == 'question':
                    question += 1
                elif value == 'consulting':
                    consulting += 1
                elif value == 'sleep':
                    sleep += 1

            for field in focus_fields:
                value = getattr(patrol, field)
                if value == '3':
                    three_count += 1
                elif value == '2':
                    two_count += 1
                elif value == '1':
                    one_count += 1
        # 결과 출력
        print("Focus가 3인 횟수:", three_count)
        print("Focus가 2인 횟수:", two_count)
        print("Focus가 1인 횟수:", one_count)
        print("국어자습:", k_ss_count)
        print("국어인강:", k_il_count)
        print("sleep", sleep)

        week_report['week_name'] = study.week_name
        week_report['study_data'] = {
            # 총시간 / 자습시간 / 인강시간 계산해서 넣어야함
        }
        week_report['focus_counts'] = {
            'three': three_count,
            'two': two_count,
            'one': one_count
        }
        week_report['study_counts'] = {
            'k_ss': k_ss_count,
            'k_il': k_il_count,
            'm_ss': m_ss_count,
            'm_il': m_il_count,
            'e_ss': e_ss_count,
            'e_il': e_il_count,
            'r_ss': r_ss_count,
            'r_il': r_il_count,
            'plan': plan,
            'mentoring': mentoring,
            'question': question,
            'consulitng': consulting,
            'sleep': sleep,
        }
        weekly_reports.append(week_report)
    context = {'weekly_reports': weekly_reports}

    return render(request, 'report/study/study_report.html', context)