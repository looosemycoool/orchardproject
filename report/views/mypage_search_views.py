from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from django.conf import settings
from collections import defaultdict

from check.models import StudentRegister, PatrolCheck
from mypage.models import Planner

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
    return render(request, 'report/mypage_search/mypage_search_main.html', context)


def mypage_search_detail(request, student_id):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    student = StudentRegister.objects.get(id=student_id)
    planner_datas = Planner.objects.filter(username_id=student.username.id, date__range=[start_date, end_date]).order_by('date')

    total_study_hours = {
        'korean_lecture_study': 0,
        'korean_self_study': 0,
        'math_lecture_study': 0,
        'math_self_study': 0,
        'english_lecture_study': 0,
        'english_self_study': 0,
        'research_lecture_study': 0,
        'research_self_study': 0,
    }

    for planner in planner_datas:
        total_study_hours['korean_lecture_study'] += (planner.korean_lecture_study_hour or 0) * 60 + (
                    planner.korean_lecture_study_min or 0)
        total_study_hours['korean_self_study'] += (planner.korean_self_study_hour or 0) * 60 + (
                    planner.korean_self_study_min or 0)
        total_study_hours['math_lecture_study'] += (planner.math_lecture_study_hour or 0) * 60 + (
                    planner.math_lecture_study_min or 0)
        total_study_hours['math_self_study'] += (planner.math_self_study_hour or 0) * 60 + (
                    planner.math_self_study_min or 0)
        total_study_hours['english_lecture_study'] += (planner.english_lecture_study_hour or 0) * 60 + (
                    planner.english_lecture_study_min or 0)
        total_study_hours['english_self_study'] += (planner.english_self_study_hour or 0) * 60 + (
                    planner.english_self_study_min or 0)
        total_study_hours['research_lecture_study'] += (planner.research_lecture_study_hour or 0) * 60 + (
                    planner.research_lecture_study_min or 0)
        total_study_hours['research_self_study'] += (planner.research_self_study_hour or 0) * 60 + (
                    planner.research_self_study_min or 0)

    # Calculate total lecture study and self-study hours
    total_korean_study = total_study_hours['korean_lecture_study'] + total_study_hours['korean_self_study']
    total_math_study = total_study_hours['math_lecture_study'] + total_study_hours['math_self_study']
    total_english_study = total_study_hours['english_lecture_study'] + total_study_hours['english_self_study']
    total_research_study = total_study_hours['research_lecture_study'] + total_study_hours['research_self_study']

    total_lecture_study = total_study_hours['korean_lecture_study'] + total_study_hours['math_lecture_study'] + \
                          total_study_hours['english_lecture_study'] + total_study_hours['research_lecture_study']

    total_self_study = total_study_hours['korean_self_study'] + total_study_hours['math_self_study'] + \
                       total_study_hours['english_self_study'] + total_study_hours['research_self_study']

    total_study_hours['total_korean_study'] = total_korean_study
    total_study_hours['total_math_study'] = total_math_study
    total_study_hours['total_english_study'] = total_english_study
    total_study_hours['total_research_study'] = total_research_study

    total_study_hours['total_lecture_study'] = total_lecture_study
    total_study_hours['total_self_study'] = total_self_study
    total_study_hours['total_study'] = total_lecture_study + total_self_study

    daily_study = {}

    for planner in planner_datas:
        # Calculate study hours for each subject for the current planner
        daily_study[planner.date] = {
            'korean_lecture_study': (planner.korean_lecture_study_hour or 0) * 60 + (planner.korean_lecture_study_min or 0),
            'korean_self_study':  (planner.korean_self_study_hour or 0) * 60 + (planner.korean_self_study_min or 0),
            'korean_study': (planner.korean_lecture_study_hour or 0) * 60 + (planner.korean_lecture_study_min or 0) + (planner.korean_self_study_hour or 0) * 60 + (planner.korean_self_study_min or 0),

            'math_lecture_study': (planner.math_lecture_study_hour or 0) * 60 + (planner.math_lecture_study_min or 0),
            'math_self_study': (planner.math_self_study_hour or 0) * 60 + (planner.math_self_study_min or 0),
            'math_study': (planner.math_lecture_study_hour or 0) * 60 + (planner.math_lecture_study_min or 0) +  (planner.math_self_study_hour or 0) * 60 + (planner.math_self_study_min or 0),

            'english_lecture_study': (planner.english_lecture_study_hour or 0) * 60 + (planner.english_lecture_study_min or 0),
            'english_self_study': (planner.english_self_study_hour or 0) * 60 + (planner.english_self_study_min or 0),
            'english_study': (planner.english_lecture_study_hour or 0) * 60 + (planner.english_lecture_study_min or 0) + (planner.english_self_study_hour or 0) * 60 + (planner.english_self_study_min or 0),

            'research_lecture_study': (planner.research_lecture_study_hour or 0) * 60 + (planner.research_lecture_study_min or 0),
            'research_self_study': (planner.research_self_study_hour or 0) * 60 + (planner.research_self_study_min or 0),
            'research_study': (planner.research_lecture_study_hour or 0) * 60 + (planner.research_lecture_study_min or 0) + (planner.research_self_study_hour or 0) * 60 + (planner.research_self_study_min or 0),

            'lecture_study': (planner.korean_lecture_study_hour or 0) * 60 + (planner.korean_lecture_study_min or 0) + (planner.math_lecture_study_hour or 0) * 60 + (planner.math_lecture_study_min or 0) + (planner.english_lecture_study_hour or 0) * 60 + (planner.english_lecture_study_min or 0) + (planner.research_lecture_study_hour or 0) * 60 + (planner.research_lecture_study_min or 0),
            'self_study': (planner.korean_self_study_hour or 0) * 60 + (planner.korean_self_study_min or 0) + (planner.math_self_study_hour or 0) * 60 + (planner.math_self_study_min or 0) + (planner.english_self_study_hour or 0) * 60 + (planner.english_self_study_min or 0) + (planner.research_self_study_hour or 0) * 60 + (planner.research_self_study_min or 0),
            'total_study': (planner.korean_lecture_study_hour or 0) * 60 + (planner.korean_lecture_study_min or 0) + (planner.math_lecture_study_hour or 0) * 60 + (planner.math_lecture_study_min or 0) + (planner.english_lecture_study_hour or 0) * 60 + (planner.english_lecture_study_min or 0) + (planner.research_lecture_study_hour or 0) * 60 + (planner.research_lecture_study_min or 0) + (planner.korean_self_study_hour or 0) * 60 + (planner.korean_self_study_min or 0) + (planner.math_self_study_hour or 0) * 60 + (planner.math_self_study_min or 0) + (planner.english_self_study_hour or 0) * 60 + (planner.english_self_study_min or 0) + (planner.research_self_study_hour or 0) * 60 + (planner.research_self_study_min or 0),
        }

    # Pass the total study hours dictionary to the template
    report = {
        'start_date': start_date,
        'end_date': end_date,
        'planner_datas': planner_datas,
        'daily_study': daily_study,
        'total_study_hours': total_study_hours,
    }

    context = {'report': report, 'student': student}
    return render(request, 'report/mypage_search/mypage_search_detail.html', context)
