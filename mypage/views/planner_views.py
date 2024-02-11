from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Planner
from ..forms import PlannerForm
from datetime import datetime
from django.contrib.auth.models import User


@login_required(login_url='common:login')
def index(request, user_id):
    today_date = datetime.today().date()
    planner_instance, created = Planner.objects.get_or_create(username_id=user_id, date=today_date)

    # POST 요청 처리
    if request.method == 'POST':
        planner_instance.username = request.user
        planner_instance.date = today_date

        # 국어 수업 정보 저장
        planner_instance.korean_lecture_study_hour = request.POST.get('korean_lecture_study_hour', '')
        planner_instance.korean_lecture_study_min = request.POST.get('korean_lecture_study_min', '')
        planner_instance.korean_self_study_hour = request.POST.get('korean_self_study_hour', '')
        planner_instance.korean_self_study_min = request.POST.get('korean_self_study_min', '')
        # 필요한 경우 시간 필드의 빈 값을 처리
        if not planner_instance.korean_lecture_study_hour:
            planner_instance.korean_lecture_study_hour = 0
        if not planner_instance.korean_lecture_study_min:
            planner_instance.korean_lecture_study_min = 0
        if not planner_instance.korean_self_study_hour:
            planner_instance.korean_self_study_hour = 0
        if not planner_instance.korean_self_study_min:
            planner_instance.korean_self_study_min = 0
        # 수학 수업 정보 저장
        planner_instance.math_lecture_study_hour = request.POST.get('math_lecture_study_hour', '')
        planner_instance.math_lecture_study_min = request.POST.get('math_lecture_study_min', '')
        planner_instance.math_self_study_hour = request.POST.get('math_self_study_hour', '')
        planner_instance.math_self_study_min = request.POST.get('math_self_study_min', '')
        # 필요한 경우 시간 필드의 빈 값을 처리
        if not planner_instance.math_lecture_study_hour:
            planner_instance.math_lecture_study_hour = 0
        if not planner_instance.math_lecture_study_min:
            planner_instance.math_lecture_study_min = 0
        if not planner_instance.math_self_study_hour:
            planner_instance.math_self_study_hour = 0
        if not planner_instance.math_self_study_min:
            planner_instance.math_self_study_min = 0
        # 영어 수업 정보 저장
        planner_instance.english_lecture_study_hour = request.POST.get('english_lecture_study_hour', '')
        planner_instance.english_lecture_study_min = request.POST.get('english_lecture_study_min', '')
        planner_instance.english_self_study_hour = request.POST.get('english_self_study_hour', '')
        planner_instance.english_self_study_min = request.POST.get('english_self_study_min', '')
        # 필요한 경우 시간 필드의 빈 값을 처리
        if not planner_instance.english_lecture_study_hour:
            planner_instance.english_lecture_study_hour = 0
        if not planner_instance.english_lecture_study_min:
            planner_instance.english_lecture_study_min = 0
        if not planner_instance.english_self_study_hour:
            planner_instance.english_self_study_hour = 0
        if not planner_instance.english_self_study_min:
            planner_instance.english_self_study_min = 0
        # 탐구 수업 정보 저장
        planner_instance.research_lecture_study_hour = request.POST.get('research_lecture_study_hour', '')
        planner_instance.research_lecture_study_min = request.POST.get('research_lecture_study_min', '')
        planner_instance.research_self_study_hour = request.POST.get('research_self_study_hour', '')
        planner_instance.research_self_study_min = request.POST.get('research_self_study_min', '')
        # 필요한 경우 시간 필드의 빈 값을 처리
        if not planner_instance.research_lecture_study_hour:
            planner_instance.research_lecture_study_hour = 0
        if not planner_instance.research_lecture_study_min:
            planner_instance.research_lecture_study_min = 0
        if not planner_instance.research_self_study_hour:
            planner_instance.research_self_study_hour = 0
        if not planner_instance.research_self_study_min:
            planner_instance.research_self_study_min = 0
        # Todo 정보 저장
        planner_instance.todo1_subject = request.POST.get('todo1_subject', '')
        planner_instance.todo1_content = request.POST.get('todo1_content', '')
        planner_instance.todo2_subject = request.POST.get('todo2_subject', '')
        planner_instance.todo2_content = request.POST.get('todo2_content', '')
        planner_instance.todo3_subject = request.POST.get('todo3_subject', '')
        planner_instance.todo3_content = request.POST.get('todo3_content', '')
        planner_instance.todo4_subject = request.POST.get('todo4_subject', '')
        planner_instance.todo4_content = request.POST.get('todo4_content', '')
        planner_instance.todo5_subject = request.POST.get('todo5_subject', '')
        planner_instance.todo5_content = request.POST.get('todo5_content', '')
        planner_instance.todo6_subject = request.POST.get('todo6_subject', '')
        planner_instance.todo6_content = request.POST.get('todo6_content', '')
        planner_instance.todo7_subject = request.POST.get('todo7_subject', '')
        planner_instance.todo7_content = request.POST.get('todo7_content', '')
        planner_instance.todo8_subject = request.POST.get('todo8_subject', '')
        planner_instance.todo8_content = request.POST.get('todo8_content', '')
        planner_instance.todo9_subject = request.POST.get('todo9_subject', '')
        planner_instance.todo9_content = request.POST.get('todo9_content', '')
        planner_instance.todo10_subject = request.POST.get('todo10_subject', '')
        planner_instance.todo10_content = request.POST.get('todo10_content', '')

        planner_instance.save()

        return redirect('mypage:planner_index', user_id=user_id)

    context = {
        'planner_instance': planner_instance,
        'today_date': today_date,
    }
    return render(request, 'mypage/planner/planner.html', context)

@login_required(login_url='common:login')
def search(request, user_id, date):

    return render(request, 'mypage/planner/planner_search.html')
@login_required(login_url='common:login')
def detail(request, user_id):
    return render(request, 'mypage/planner/planner_detail.html')