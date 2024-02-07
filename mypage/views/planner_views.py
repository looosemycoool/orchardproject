from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Planner
from ..forms import PlannerForm
from datetime import datetime
from django.contrib.auth.models import User

@login_required(login_url='common:login')
def index(request, user_id):
    today_date = datetime.today().date()
    planner = Planner.objects.filter(username_id=user_id, username__planner__date=today_date).first()

    # Logic to handle form submission
    if request.method == 'POST':
        form = PlannerForm(request.POST, instance=planner)
        if form.is_valid():
            # Save the form data to the database or perform any other required action
            current_user = request.user

            # Save the form data to the database and set the logged-in user as the username
            planner_instance = form.save(commit=False)
            planner_instance.username = current_user
            planner_instance.save()
            # Redirect to the same page to prevent form resubmission
            return redirect('mypage:planner_index', user_id=user_id)
    else:
        form = PlannerForm(instance=planner)

    context = {
        'form': form,
        'today_date': today_date,
    }

    return render(request, 'mypage/planner/planner.html', context)

@login_required(login_url='common:login')
def search(request, user_id, date):
    planner = Planner.objects.filter(username_id=user_id, username__planner__date=date).first()

    # Logic to handle form submission
    if request.method == 'POST':
        form = PlannerForm(request.POST, instance=planner)
        if form.is_valid():
            # Save the form data to the database or perform any other required action
            current_user = request.user

            # Save the form data to the database and set the logged-in user as the username
            planner_instance = form.save(commit=False)
            planner_instance.username = current_user
            planner_instance.date = date
            planner_instance.save()
            # Redirect to the same page to prevent form resubmission
            return redirect('mypage:planner_search', user_id=user_id, date=date)
    else:
        form = PlannerForm(instance=planner)

    context = {
        'form': form,
    }
    return render(request, 'mypage/planner/planner_search.html', context)
@login_required(login_url='common:login')
def detail(request, user_id):
    return render(request, 'mypage/planner/planner_detail.html')