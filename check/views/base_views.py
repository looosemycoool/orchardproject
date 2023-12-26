from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from ..models import Attendance

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def index(request):
    # 과거 출석부 보는 코드
    #student = Attendance.objects.get(student_id=request.user.id)
    #context = {'student': student}
    return render(request, 'check/check_main.html')
