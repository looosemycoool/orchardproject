from django.shortcuts import render, redirect
from ..models import Patrol_Data, Student_Study_Data, Patrol_Weekly_Data, Total_Weekly_Study_Data, Average_Patrol_Data
from django.db.models import Sum, Func
from django.db.models import Avg, FloatField
from django.db.models.functions import Cast


def index(request):
    patrol_weekly_data_week_name = Patrol_Weekly_Data.objects.values('week_name').order_by('week_name').distinct()
    patrol_dates = Patrol_Data.objects.values('date').order_by('date').distinct()
    total_week_name = Total_Weekly_Study_Data.objects.values('week_name').order_by('week_name').distinct()

    context = {
        'unique_patrol_week_names': patrol_weekly_data_week_name,
        'unique_patrol_dates': patrol_dates,
        'unique_total_week_name': total_week_name,
    }
    return render(request, 'manager/data/data_main.html', context)


def create_week_patrol_data(request):
    patrol_data = Patrol_Data.objects.all()
    unique_date = patrol_data.values('date').distinct()

    if request.method == 'POST':
        week_name = request.POST.get('week_name')
        start_date = request.POST.get('start_patrol_date')
        end_date = request.POST.get('end_patrol_date')

        # 학생별로 일주일치 데이터 누적
        student_data = Patrol_Data.objects.filter(date__range=[start_date, end_date]).values(
            'student_name').annotate(
            total_k_ss_count=Sum('k_ss_count'),
            total_k_il_count=Sum('k_il_count'),
            total_m_ss_count=Sum('m_ss_count'),
            total_m_il_count=Sum('m_il_count'),
            total_e_ss_count=Sum('e_ss_count'),
            total_e_il_count=Sum('e_il_count'),
            total_r_ss_count=Sum('r_ss_count'),
            total_r_il_count=Sum('r_il_count'),
            total_plan=Sum('plan'),
            total_mentoring=Sum('mentoring'),
            total_question=Sum('question'),
            total_consulting=Sum('consulting'),
            total_sleep=Sum('sleep'),
            total_focus_three=Sum('focus_three'),
            total_focus_two=Sum('focus_two'),
            total_focus_one=Sum('focus_one'),
            total_focus_count=Sum('total_focus_count'),
        )

        # 주차별 데이터를 생성하고 Patrol_Weekly_Data에 저장
        for data in student_data:
            student_name = data['student_name']
            total_k_ss_count = data['total_k_ss_count']
            total_k_il_count = data['total_k_il_count']
            total_m_ss_count = data['total_m_ss_count']
            total_m_il_count = data['total_m_il_count']
            total_e_ss_count = data['total_e_ss_count']
            total_e_il_count = data['total_e_il_count']
            total_r_ss_count = data['total_r_ss_count']
            total_r_il_count = data['total_r_il_count']
            total_plan = data['total_plan']
            total_mentoring = data['total_mentoring']
            total_question = data['total_question']
            total_consulting = data['total_consulting']
            total_sleep = data['total_sleep']
            total_focus_three = data['total_focus_three']
            total_focus_two = data['total_focus_two']
            total_focus_one = data['total_focus_one']
            total_focus_count = data['total_focus_count']

            # 주차별 데이터를 Patrol_Weekly_Data에 저장
            patrol_weekly_data = Patrol_Weekly_Data(
                week_name=week_name,
                week_start_date=start_date,
                week_end_date=end_date,
                student_name=student_name,

                total_k_ss_count=total_k_ss_count,
                total_k_il_count=total_k_il_count,
                total_m_ss_count=total_m_ss_count,
                total_m_il_count=total_m_il_count,
                total_e_ss_count=total_e_ss_count,
                total_e_il_count=total_e_il_count,
                total_r_ss_count=total_r_ss_count,
                total_r_il_count=total_r_il_count,
                total_plan=total_plan,
                total_mentoring=total_mentoring,
                total_question=total_question,
                total_consulting=total_consulting,
                total_sleep=total_sleep,
                total_focus_three=total_focus_three,
                total_focus_two=total_focus_two,
                total_focus_one=total_focus_one,
                total_focus_count=total_focus_count,
            )
            patrol_weekly_data.save()

            patrol_dates = Patrol_Data.objects.values('date').distinct()
            total_week_name = Total_Weekly_Study_Data.objects.values('week_name').distinct()

        return redirect("manager:patrol_weekly_data_success")
    patrol_weekly_data_week_name = Patrol_Weekly_Data.objects.values('week_name').order_by('week_name').distinct()
    patrol_dates = Patrol_Data.objects.values('date').order_by('date').distinct()
    total_week_name = Total_Weekly_Study_Data.objects.values('week_name').order_by('week_name').distinct()

    context = {'unique_date': unique_date, "unique_patrol_dates": patrol_dates, "unique_total_week_name": total_week_name,
               "unique_patrol_week_names": patrol_weekly_data_week_name}
    return render(request, 'manager/data/create_week_patrol_data.html', context)


def create_total_study_data(request):
    if request.method == 'POST':
        student_study_data_week_name = request.POST.get('student_study_data_week_name')
        patrol_weekly_data_week_name = request.POST.get('patrol_weekly_data_week_name')

        # 선택한 주차에 해당하는 학과습 데이터와 순찰 일지 데이터를 가져옵니다.
        student_study_data = Student_Study_Data.objects.filter(week_name=student_study_data_week_name)
        patrol_weekly_data = Patrol_Weekly_Data.objects.filter(week_name=patrol_weekly_data_week_name)

        # 학생 이름을 기준으로 데이터를 합칩니다.
        total_study_data = []
        for student_data in student_study_data:
            student_name = student_data.student_name
            # 해당 학생 이름과 일치하는 순찰 일지 데이터를 가져옵니다.
            matching_patrol_data = patrol_weekly_data.filter(student_name=student_name)

            # 학과습 데이터와 순찰 일지 데이터를 합쳐서 Total_Weekly_Study_Data 객체를 생성합니다.
            for patrol_data in matching_patrol_data:
                total_data = Total_Weekly_Study_Data(
                    week_name=student_study_data_week_name,
                    week_start_date=patrol_data.week_start_date,
                    week_end_date=patrol_data.week_end_date,
                    student_name=student_name,
                    research1=student_data.research1,
                    research2=student_data.research2,
                    korean_lecture_study=student_data.korean_lecture_study,
                    korean_self_study=student_data.korean_self_study,
                    math_lecture_study=student_data.math_lecture_study,
                    math_self_study=student_data.math_self_study,
                    english_lecture_study=student_data.english_lecture_study,
                    english_self_study=student_data.english_self_study,
                    research1_lecture_study=student_data.research1_lecture_study,
                    research1_self_study=student_data.research1_self_study,
                    research2_lecture_study=student_data.research2_lecture_study,
                    research2_self_study=student_data.research2_self_study,
                    total_study_time=student_data.total_study_time,
                    total_k_ss_count=patrol_data.total_k_ss_count,
                    total_k_il_count=patrol_data.total_k_il_count,
                    total_m_ss_count=patrol_data.total_m_ss_count,
                    total_m_il_count=patrol_data.total_m_il_count,
                    total_e_ss_count=patrol_data.total_e_ss_count,
                    total_e_il_count=patrol_data.total_e_il_count,
                    total_r_ss_count=patrol_data.total_r_ss_count,
                    total_r_il_count=patrol_data.total_r_il_count,
                    total_plan=patrol_data.total_plan,
                    total_mentoring=patrol_data.total_mentoring,
                    total_question=patrol_data.total_question,
                    total_consulting=patrol_data.total_consulting,
                    total_sleep=patrol_data.total_sleep,
                    total_focus_three=patrol_data.total_focus_three,
                    total_focus_two=patrol_data.total_focus_two,
                    total_focus_one=patrol_data.total_focus_one,
                    total_focus_count=patrol_data.total_focus_count
                )
                total_study_data.append(total_data)
        # Total_Weekly_Study_Data를 저장합니다.
        Total_Weekly_Study_Data.objects.bulk_create(total_study_data)

        return render(request, 'manager/data/total_study_data_success.html')

    student_study_data_week_name = Student_Study_Data.objects.values('week_name').distinct()
    patrol_weekly_data_week_name = Patrol_Weekly_Data.objects.values('week_name').order_by('week_name').distinct()
    patrol_dates = Patrol_Data.objects.values('date').order_by('date').distinct()
    total_week_name = Total_Weekly_Study_Data.objects.values('week_name').order_by('week_name').distinct()

    context = {
        'student_study_data_week_name': student_study_data_week_name,
        'unique_patrol_week_name': patrol_weekly_data_week_name,
        "unique_patrol_dates": patrol_dates,
        "unique_total_week_name": total_week_name
    }
    return render(request, 'manager/data/create_total_study_data.html', context)


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 1)'


def create_average_patrol_data(request):
    if request.method == 'POST':
        patrol_weekly_data_week_name = request.POST.get('patrol_weekly_data_week_name')

        # 주차에 해당하는 학생들의 평균 카운트 계산
        patrol_weekly_data = Patrol_Weekly_Data.objects.filter(week_name=patrol_weekly_data_week_name)
        average_k_ss_count = \
            patrol_weekly_data.aggregate(average_k_ss_count=Round(Avg('total_k_ss_count'), output_field=FloatField()))[
                'average_k_ss_count']
        average_k_il_count = \
            patrol_weekly_data.aggregate(average_k_il_count=Round(Avg('total_k_il_count'), output_field=FloatField()))[
                'average_k_il_count']
        average_m_ss_count = \
            patrol_weekly_data.aggregate(average_m_ss_count=Round(Avg('total_m_ss_count'), output_field=FloatField()))[
                'average_m_ss_count']
        average_m_il_count = \
            patrol_weekly_data.aggregate(average_m_il_count=Round(Avg('total_m_il_count'), output_field=FloatField()))[
                'average_m_il_count']
        average_e_ss_count = \
            patrol_weekly_data.aggregate(average_e_ss_count=Round(Avg('total_e_ss_count'), output_field=FloatField()))[
                'average_e_ss_count']
        average_e_il_count = \
            patrol_weekly_data.aggregate(average_e_il_count=Round(Avg('total_e_il_count'), output_field=FloatField()))[
                'average_e_il_count']
        average_r_ss_count = \
            patrol_weekly_data.aggregate(average_r_ss_count=Round(Avg('total_r_ss_count'), output_field=FloatField()))[
                'average_r_ss_count']
        average_r_il_count = \
            patrol_weekly_data.aggregate(average_r_il_count=Round(Avg('total_r_il_count'), output_field=FloatField()))[
                'average_r_il_count']
        average_plan = patrol_weekly_data.aggregate(average_plan=Round(Avg('total_plan'), output_field=FloatField()))[
            'average_plan']
        average_mentoring = \
            patrol_weekly_data.aggregate(average_mentoring=Round(Avg('total_mentoring'), output_field=FloatField()))[
                'average_mentoring']
        average_question = \
            patrol_weekly_data.aggregate(average_question=Round(Avg('total_question'), output_field=FloatField()))[
                'average_question']
        average_consulting = \
            patrol_weekly_data.aggregate(average_consulting=Round(Avg('total_consulting'), output_field=FloatField()))[
                'average_consulting']
        average_sleep = \
            patrol_weekly_data.aggregate(average_sleep=Round(Avg('total_sleep'), output_field=FloatField()))[
                'average_sleep']
        average_focus_three = \
            patrol_weekly_data.aggregate(
                average_focus_three=Round(Avg('total_focus_three'), output_field=FloatField()))[
                'average_focus_three']
        average_focus_two = \
            patrol_weekly_data.aggregate(average_focus_two=Round(Avg('total_focus_two'), output_field=FloatField()))[
                'average_focus_two']
        average_focus_one = \
            patrol_weekly_data.aggregate(average_focus_one=Round(Avg('total_focus_one'), output_field=FloatField()))[
                'average_focus_one']
        average_total_focus_count = patrol_weekly_data.aggregate(
            average_total_focus_count=Round(Avg('total_focus_count'), output_field=FloatField()))[
            'average_total_focus_count']

        # Average_Patrol_Data 모델에 데이터 저장
        average_patrol_data = Average_Patrol_Data(
            week_name=patrol_weekly_data_week_name,
            average_k_ss_count=average_k_ss_count,
            average_k_il_count=average_k_il_count,
            average_m_ss_count=average_m_ss_count,
            average_m_il_count=average_m_il_count,
            average_e_ss_count=average_e_ss_count,
            average_e_il_count=average_e_il_count,
            average_r_ss_count=average_r_ss_count,
            average_r_il_count=average_r_il_count,
            average_plan=average_plan,
            average_mentoring=average_mentoring,
            average_question=average_question,
            average_consulting=average_consulting,
            average_sleep=average_sleep,
            average_focus_three=average_focus_three,
            average_focus_two=average_focus_two,
            average_focus_one=average_focus_one,
            average_total_focus_count=average_total_focus_count,
        )
        average_patrol_data.save()

        return render(request, 'manager/data/total_study_data_success.html')

    patrol_weekly_data_week_name = Patrol_Weekly_Data.objects.values('week_name').distinct()

    context = {
        'patrol_weekly_data_week_name': patrol_weekly_data_week_name
    }
    return render(request, 'manager/data/create_average_patrol_data.html', context)


def patrol_weekly_data_success(request):
    return render(request, 'manager/data/patrol_weekly_data_success.html')
