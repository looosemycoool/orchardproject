from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# from ..models import Reserve, Teacher, Notice
from django.contrib.auth.models import User

@login_required(login_url='common:login')
def index(request, user_id):
    return render(request, 'mypage/mypage_main.html')