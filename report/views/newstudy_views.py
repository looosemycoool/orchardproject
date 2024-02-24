from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from django.conf import settings
from collections import defaultdict

from check.models import StudentRegister, PatrolCheck
from mypage.models import Planner
from manager.models import Student_Study_Data, WeekPlan

def index(request):
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
    return render(request, 'report/newstudy/newstudy_main.html', context)

def newstudy_report(request, student_id):
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
    planner_fields = [
        'korean_lecture_study_hour', 'korean_lecture_study_min', 'korean_self_study_hour', 'korean_self_study_min',
        'math_lecture_study_hour', 'math_lecture_study_min', 'math_self_study_hour', 'math_self_study_min',
        'english_lecture_study_hour', 'english_lecture_study_min', 'english_self_study_hour', 'english_self_study_min',
        'research_lecture_study_hour', 'research_lecture_study_min', 'research_self_study_hour', 'research_self_study_min',
    ]

    week_plan_datas = WeekPlan.objects.filter(user__id=student_id).order_by('-id')
    print(week_plan_datas)
    # study_datas = Student_Study_Data.objects.filter(user__id=student_id).order_by('-id')
    student = StudentRegister.objects.get(id=student_id, is_dropped=False)
    # print(student.username)
    weekly_reports = []

    # 각자 학생들의 patrol 데이터
    for week_plan in week_plan_datas:
        week_report = {}

        ##### 일일 순찰 데이터 #####
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

        ##### 주간 학습 계획 데이터 #####
        week_plan_korean_study = 0
        week_plan_korean_lecture_study = 0
        week_plan_korean_self_study = 0
        week_plan_math_study = 0
        week_plan_math_lecture_study = 0
        week_plan_math_self_study = 0
        week_plan_english_study = 0
        week_plan_english_lecture_study = 0
        week_plan_english_self_study = 0
        week_plan_research_study = 0
        week_plan_research_lecture_study = 0
        week_plan_research_self_study = 0

        # 각 요일을 반복하며 해당 요일의 한국어 강의 및 자습 시간을 누적합니다.
        for day in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']:
            # 각 요일의 강의 시간을 분 단위로 누적합니다.
            week_plan_korean_lecture_study += getattr(week_plan, f"{day}_korean_lecture_study_hour", 0) * 60
            # 각 요일의 자습 시간을 분 단위로 누적합니다.
            week_plan_korean_self_study += getattr(week_plan, f"{day}_korean_self_study_hour", 0) * 60
            # 각 요일의 강의 및 자습 분을 누적합니다.
            week_plan_korean_lecture_study += getattr(week_plan, f"{day}_korean_lecture_study_min", 0)
            week_plan_korean_self_study += getattr(week_plan, f"{day}_korean_self_study_min", 0)
            week_plan_korean_study = week_plan_korean_lecture_study + week_plan_korean_self_study

            week_plan_math_lecture_study += getattr(week_plan, f"{day}_math_lecture_study_hour", 0) * 60
            # 각 요일의 자습 시간을 분 단위로 누적합니다.
            week_plan_math_self_study += getattr(week_plan, f"{day}_math_self_study_hour", 0) * 60
            # 각 요일의 강의 및 자습 분을 누적합니다.
            week_plan_math_lecture_study += getattr(week_plan, f"{day}_math_lecture_study_min", 0)
            week_plan_math_self_study += getattr(week_plan, f"{day}_math_self_study_min", 0)
            week_plan_math_study = week_plan_math_lecture_study + week_plan_math_self_study

            week_plan_english_lecture_study += getattr(week_plan, f"{day}_english_lecture_study_hour", 0) * 60
            # 각 요일의 자습 시간을 분 단위로 누적합니다.
            week_plan_english_self_study += getattr(week_plan, f"{day}_english_self_study_hour", 0) * 60
            # 각 요일의 강의 및 자습 분을 누적합니다.
            week_plan_english_lecture_study += getattr(week_plan, f"{day}_english_lecture_study_min", 0)
            week_plan_english_self_study += getattr(week_plan, f"{day}_english_self_study_min", 0)
            week_plan_english_study = week_plan_english_lecture_study + week_plan_english_self_study

            week_plan_research_lecture_study += getattr(week_plan, f"{day}_research_lecture_study_hour", 0) * 60
            # 각 요일의 자습 시간을 분 단위로 누적합니다.
            week_plan_research_self_study += getattr(week_plan, f"{day}_research_self_study_hour", 0) * 60
            # 각 요일의 강의 및 자습 분을 누적합니다.
            week_plan_research_lecture_study += getattr(week_plan, f"{day}_research_lecture_study_min", 0)
            week_plan_research_self_study += getattr(week_plan, f"{day}_research_self_study_min", 0)
            week_plan_research_study = week_plan_research_lecture_study + week_plan_research_self_study

        print('week_plan_research_study: ' ,week_plan_research_study)

        total_student_datas = Planner.objects.filter(date__gte=week_plan.start_date, date__lte=week_plan.end_date)
        student_number = len(total_student_datas)

        ##### 학생 개별 마이페이지 플래너 시간 #####
        my_korean_study = 0
        my_korean_lecture_study = 0
        my_korean_self_study = 0

        my_math_study = 0
        my_math_lecture_study = 0
        my_math_self_study = 0

        my_english_study = 0
        my_english_lecture_study = 0
        my_english_self_study = 0

        my_research_study = 0
        my_research_lecture_study = 0
        my_research_self_study = 0

        my_lecture_study = 0
        my_self_study = 0
        my_total_study = 0


        # for data in total_student_datas:
        #     total_korean_study += data.korean_study
        #     total_korean_self_study += data.korean_self_study
        #     total_math_study += data.math_study
        #     total_math_self_study += data.math_self_study
        #     total_english_study += data.english_study
        #     total_english_self_study += data.english_self_study
        #     total_research1_study += data.research1_study
        #     total_research1_self_study += data.research1_self_study
        #     total_research2_study += data.research2_study
        #     total_research2_self_study += data.research2_self_study
        #
        # average_total_study = int(total_korean_study + total_math_study + total_english_study + total_research1_study + total_research2_study) / student_number
        # average_total_self_study = int(total_korean_self_study + total_math_self_study + total_english_self_study + total_research1_self_study + total_research2_self_study / student_number) / student_number
        # average_total_lecture_study = average_total_study - average_total_self_study

        patrol_datas = PatrolCheck.objects.filter(date__gte=week_plan.start_date, date__lte=week_plan.end_date, user__id=student_id)
        planner_datas = Planner.objects.filter(date__gte=week_plan.start_date, date__lte=week_plan.end_date, username=student.username)
        print(planner_datas)

        ## 학생 개인 일일순찰 데이터
        for patrol in patrol_datas:
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

        ## 학생 개인 마이페이지 데이터
        for planner in planner_datas:
            if planner.korean_lecture_study_hour is not None:
                my_korean_lecture_study += planner.korean_lecture_study_hour * 60
            if planner.korean_lecture_study_min is not None:
                my_korean_lecture_study += planner.korean_lecture_study_min
            if planner.korean_self_study_hour is not None:
                my_korean_self_study += planner.korean_self_study_hour * 60
            if planner.korean_self_study_min is not None:
                my_korean_self_study += planner.korean_self_study_min

            if planner.math_lecture_study_hour is not None:
                my_math_lecture_study += planner.math_lecture_study_hour * 60
            if planner.math_lecture_study_min is not None:
                my_math_lecture_study += planner.math_lecture_study_min
            if planner.math_self_study_hour is not None:
                my_math_self_study += planner.math_self_study_hour * 60
            if planner.math_self_study_min is not None:
                my_math_self_study += planner.math_self_study_min

            if planner.english_lecture_study_hour is not None:
                my_english_lecture_study += planner.english_lecture_study_hour * 60
            if planner.english_lecture_study_min is not None:
                my_english_lecture_study += planner.english_lecture_study_min
            if planner.english_self_study_hour is not None:
                my_english_self_study += planner.english_self_study_hour * 60
            if planner.english_self_study_min is not None:
                my_english_self_study += planner.english_self_study_min

            if planner.research_lecture_study_hour is not None:
                my_research_lecture_study += planner.research_lecture_study_hour * 60
            if planner.research_lecture_study_min is not None:
                my_research_lecture_study += planner.research_lecture_study_min
            if planner.research_self_study_hour is not None:
                my_research_self_study += planner.research_self_study_hour * 60
            if planner.research_self_study_min is not None:
                my_research_self_study += planner.research_self_study_min

        my_korean_study = my_korean_lecture_study + my_korean_self_study
        my_math_study = my_math_lecture_study + my_math_self_study
        my_english_study = my_english_lecture_study + my_english_self_study
        my_research_study = my_research_lecture_study + my_research_self_study

        my_lecture_study = my_korean_lecture_study + my_math_lecture_study + my_english_lecture_study + my_research_lecture_study
        my_self_study = my_korean_self_study + my_math_self_study + my_english_self_study + my_research_self_study

        my_total_study = my_lecture_study + my_self_study

        print('국어 강의시간', my_korean_lecture_study)
        print('수학 강의시간', my_math_lecture_study)
        print('영어 강의시간', my_english_lecture_study)
        print('탐구 강의시간', my_research_lecture_study)
        print('강의시간', my_lecture_study)

        # focus score 공식
        total_focus_count = three_count + two_count + one_count

        if total_focus_count == 0:
            focus_score = 0
        else:
            # 집중도 단순 평균 공식
            focus_score = round(((three_count * 3) + (two_count * 2) + one_count) / total_focus_count, 2)

            # 집중도 퍼센트 공식
            # three_focus_percent = (three_count / total_focus_count) * 100
            # two_focus_percent = (two_count / total_focus_count) * 100
            # one_focus_percent = (one_count / total_focus_count) * 100

            # focus_score = round((three_focus_percent * 1) + (two_focus_percent * 0.5) + (
            #             one_focus_percent * -1), 2)

        # week_report에 저장
        week_report['student_name'] = week_plan.user.student
        week_report['week_name'] = week_plan.week_name
        week_report['start_date'] = week_plan.start_date
        week_report['end_date'] = week_plan.end_date

        ## 주간 학습 계획 데이터 # 수강시간 / 자습시간 변경으로 코드 바뀜
        week_report['week_plan'] = {
            # 총시간 / 자습시간 / 인강시간 계산해서 넣어야함 -> 학생 개인의 데이터
            'week_plan_korean_study': week_plan_korean_study,
            'week_plan_korean_lecture_study': week_plan_korean_lecture_study,
            'week_plan_korean_self_study': week_plan_korean_self_study,

            'week_plan_math_study': week_plan_math_study,
            'week_plan_math_lecture_study': week_plan_math_lecture_study,
            'week_plan_math_self_study': week_plan_math_self_study,

            'week_plan_english_study': week_plan_english_study,
            'week_plan_english_lecture_study': week_plan_english_lecture_study,
            'week_plan_english_self_study': week_plan_english_self_study,

            'week_plan_research_study': week_plan_research_study,
            'week_plan_research_lecture_study': week_plan_research_lecture_study,
            'week_plan_research_self_study': week_plan_research_self_study,
        }
        ## 마이페이지에 저장한 데이터
        week_report['my_data'] = {
            'my_korean_study': my_korean_study,
            'my_korean_lecture_study': my_korean_lecture_study,
            'my_korean_self_study': my_korean_self_study,

            'my_math_study': my_math_study,
            'my_math_lecture_study': my_math_lecture_study,
            'my_math_self_study': my_math_self_study,

            'my_english_study': my_english_study,
            'my_english_lecture_study': my_english_lecture_study,
            'my_english_self_study': my_english_self_study,

            'my_research_study': my_research_study,
            'my_research_lecture_study': my_research_lecture_study,
            'my_research_self_study': my_research_self_study,

            'my_lecture_study': my_lecture_study,
            'my_self_study': my_self_study,
            'my_total_study': my_total_study,

            'my_study_hour': (my_total_study / 60),
            'my_study_min': (my_total_study % 60),
            'my_self_study_hour': (my_self_study / 60),
            'my_self_study_min': (my_self_study % 60),
            'my_lecture_study_hour': (my_lecture_study / 60),
            'my_lecture_study_min': (my_lecture_study % 60)
        }
        week_report['focus_score'] = {
            'focus_score': focus_score
        }
        week_report['focus_counts'] = {
            'three': three_count,
            'two': two_count,
            'one': one_count
        }
        ##### 곱하기 x 30분으로 시간으로 계산해야함
        week_report['study_counts'] = {
            'k_ss': k_ss_count,
            'k_il': k_il_count,
            'korean_total': k_ss_count + k_il_count,

            'm_ss': m_ss_count,
            'm_il': m_il_count,
            'math_total': m_ss_count + m_il_count,

            'e_ss': e_ss_count,
            'e_il': e_il_count,
            'english_total': e_ss_count + e_il_count,

            'r_ss': r_ss_count,
            'r_il': r_il_count,
            'research_total': r_ss_count + r_il_count,

            # 'total_'
            'total_study_count': k_ss_count + k_il_count + m_ss_count + m_il_count + e_ss_count + e_il_count + r_ss_count + r_il_count,

            'plan': plan,
            'mentoring': mentoring,
            'question': question,
            'consulting': consulting,
            'sleep': sleep,
        }
        # week_report['average_data'] = {
        #     'average_korean_lecture_study': int((total_korean_study - total_korean_self_study) / student_number),
        #     'average_korean_self_study': int(total_korean_self_study / student_number),
        #     'average_math_lecture_study': int((total_math_study - total_math_self_study) / student_number),
        #     'average_math_self_study': int(total_math_self_study / student_number),
        #     'average_english_lecture_study': int((total_english_study - total_english_self_study) / student_number),
        #     'average_english_self_study': int(total_english_self_study / student_number),
        #     'average_research_lecture_study': int(((total_research1_study) - (total_research1_self_study)) / student_number),
        #     'average_research_self_study': int((total_research1_self_study + total_research2_self_study) / student_number),
        #     'average_total_lecture_study': average_total_lecture_study,
        #     'average_total_self_study': average_total_self_study,
        #     'average_total_study': average_total_study
        # }
        weekly_reports.append(week_report)
    context = {'weekly_reports': weekly_reports, 'student': student}

    return render(request, 'report/newstudy/newstudy_report.html', context)