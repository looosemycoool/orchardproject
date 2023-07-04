from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def index(request):
    return render(request, 'manager/manager_main.html')
