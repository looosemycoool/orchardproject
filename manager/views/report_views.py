from django.shortcuts import render, redirect
from ..models import Student_Study_Data, Patrol_Data, Total_Weekly_Study_Data, Average_Study_Data, Average_Patrol_Data
from reserve.models import Reserve
from django.db.models import Min
from datetime import datetime
from django.contrib.auth.models import User

def report_study_main(request):
    total_weekly_study_data = Total_Weekly_Study_Data.objects.all()

    unique_week = total_weekly_study_data.values('week_name').distinct()
    student_names = total_weekly_study_data.values('student_name').distinct()

    context = {'total_weekly_study_data': total_weekly_study_data, 'student_names': student_names,
               'unique_week': unique_week}
    return render(request, 'manager/report/study/study_main.html', context)


def report_study_detail(request):
    student_name = request.GET.get('student_name')
    start_week = request.GET.get('start_week')
    end_week = request.GET.get('end_week')

    total_weekly_study_data = Total_Weekly_Study_Data.objects.all()

    unique_week = total_weekly_study_data.values('week_name').distinct()
    student_names = total_weekly_study_data.values('student_name').distinct()

    filtered_data = Total_Weekly_Study_Data.objects.filter(
        student_name=student_name,
        week_name__range=[start_week, end_week]
    )
    average_data = Average_Study_Data.objects.filter(
        week_name__range=[start_week, end_week]
    )
    average_patrol_data = Average_Patrol_Data.objects.filter(
        week_name__range=[start_week, end_week]
    )
    total_time_data = Total_Weekly_Study_Data.objects.filter(
        week_name__range=[start_week, end_week]
    )

    week_data = {}  # 주차별 데이터를 저장할 딕셔너리

    for data in total_time_data:
        week = data.week_name
        if week not in week_data:
            week_data[week] = []
        week_data[week].append(data.total_study_time)

    combined_data = []

    # Calculate focus_index for each filtered_data object
    for data in filtered_data:
        total_focus_count = data.total_focus_count
        if total_focus_count != 0:
            data.focus_three_percentage = (data.total_focus_three / total_focus_count) * 100
            data.focus_two_percentage = (data.total_focus_two / total_focus_count) * 100
            data.focus_one_percentage = (data.total_focus_one / total_focus_count) * 100
        else:
            data.focus_three_percentage = 0
            data.focus_two_percentage = 0
            data.focus_one_percentage = 0

        # Calculate overall focus score
        focus_score = (data.focus_three_percentage * 1) + (data.focus_two_percentage * 0.5) + (
                data.focus_one_percentage * -1)
        data.focus_index = round(focus_score, 2)

        # patrol 과목별 합산 횟수
        data.week_korean_study_count = data.total_k_ss_count + data.total_k_il_count
        data.week_math_study_count = data.total_m_ss_count + data.total_m_il_count
        data.week_english_study_count = data.total_e_ss_count + data.total_e_il_count
        data.week_research_study_count = data.total_r_ss_count + data.total_r_il_count

        # patrol 자습 / 인강 합산
        data.week_ss_count = data.total_k_ss_count + data.total_m_ss_count + data.total_e_ss_count + data.total_r_ss_count
        data.week_il_count = data.total_k_il_count + data.total_m_il_count + data.total_e_il_count + data.total_r_il_count
        data.week_study_total_count = data.week_ss_count + data.week_il_count

        # 학과습 과목별 합산
        data.week_korean_study_time = data.korean_lecture_study + data.korean_self_study
        data.week_math_study_time = data.math_lecture_study + data.math_self_study
        data.week_english_study_time = data.english_lecture_study + data.english_self_study
        data.week_research1_study_time = data.research1_lecture_study + data.research1_self_study
        data.week_research2_study_time = data.research2_lecture_study + data.research2_self_study

        # 학과습 탐구 자습 / 인강 합산
        data.week_research_lecture_study_time = data.research1_lecture_study + data.research2_lecture_study
        data.week_research_self_study_time = data.research2_self_study + data.research1_self_study

        # 학과습 자습 / 인강 합산
        data.week_self_study_time = data.korean_self_study + data.math_self_study + data.english_self_study + data.research1_self_study + data.research2_self_study
        data.week_lecture_study_time = data.korean_lecture_study + data.math_lecture_study + data.english_lecture_study + data.research1_lecture_study + data.research2_lecture_study
        data.week_total_study_time = data.korean_self_study + data.math_self_study + data.english_self_study + data.research1_self_study + data.research2_self_study + data.korean_lecture_study + data.math_lecture_study + data.english_lecture_study + data.research1_lecture_study + data.research2_lecture_study

        # 시간 / 분 나누기
        data.week_self_study_time_hour = data.week_self_study_time // 60
        data.week_self_study_time_min = data.week_self_study_time % 60
        data.week_lecture_study_time_hour = data.week_lecture_study_time // 60
        data.week_lecture_study_time_min = data.week_lecture_study_time % 60
        data.week_total_study_time_hour = data.week_total_study_time // 60
        data.week_total_study_time_min = data.week_total_study_time % 60

    total_weekly_study_data = Total_Weekly_Study_Data.objects.all()

    for data in filtered_data:
        combined_data.append({
            'filtered': data,
            'average': None  # 초기값으로 None을 설정
        })

    for average in average_data:
        # average_data의 week_name과 filtered_data의 week_name이 일치하는지 확인하여 연결
        for data in combined_data:
            if data['filtered'].week_name == average.week_name:
                data['average'] = average
                break

    context = {
        'student_name': student_name,
        'combined_data': combined_data,
        # 'student_total_study_time': student_total_study_time,
        'week_data': week_data,
        'start_week': start_week,
        'end_week': end_week,
        'unique_week': unique_week,
        'student_names': student_names,
        'total_weekly_study_data': total_weekly_study_data
    }
    return render(request, 'manager/report/study/study_detail.html', context)

def report_consulting_main(request):
    reserve_data = Reserve.objects.all()
    student_names = reserve_data.values('student_name__first_name').distinct()
    date = reserve_data.values('date').order_by('date').distinct()
    context = {
        'student_names': student_names,
        'date': date,
    }
    return render(request, 'manager/report/consulting/consulting_main.html', context)

def report_consulting_detail(request):
    student_name = request.GET.get('student_name')
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    reserve_data = Reserve.objects.all()
    student = User.objects.get(first_name=student_name)
    student_names = reserve_data.values('student_name__first_name').distinct()
    date = reserve_data.values('date').annotate(min_date=Min('date')).order_by('date')

    start_date = datetime.strptime(start_date_str, '%Y년 %m월 %d일').date()
    end_date = datetime.strptime(end_date_str, '%Y년 %m월 %d일').date()

    if student:
        filtered_data_korean = Reserve.objects.filter(
            student_name_id=student.id,
            teacher_id=1,
            date__range=[start_date, end_date]
        )
        filtered_data_math = Reserve.objects.filter(
            student_name_id=student.id,
            teacher_id__in=[2, 3],
            date__range=[start_date, end_date]
        )
        filtered_data_english = Reserve.objects.filter(
            student_name_id=student.id,
            date__range=[start_date, end_date]
        )
        filtered_data_research = Reserve.objects.filter(
            student_name_id=student.id,
            teacher_id__in=[5, 6, 9],
            date__range=[start_date, end_date]
        )
    else:
        # student가 없을 경우, 빈 쿼리셋 반환
        filtered_data = Reserve.objects.none()

    context = {
        'student_names': student_names,
        'date': date,
        'student': student,
        # 'filtered_data': filtered_data,
        'filtered_data_math': filtered_data_math,
        'filtered_data_korean': filtered_data_korean,
        'filtered_data_english': filtered_data_english,
        'filtered_data_research': filtered_data_research,
    }
    return render(request, 'manager/report/consulting/consulting_detail.html', context)

def report_grade_main(request):
    return render(request, 'manager/report/grade_data/grade_main.html')

