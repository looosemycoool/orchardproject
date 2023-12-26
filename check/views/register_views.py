from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from ..models import Attendance, BreakUser, StudentRegister
from ..forms import StudentRegisterForm

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def index(request):
    #student = Attendance.objects.get(student_id=request.user.id)
    #context = {'student': student}
    return render(request, 'check/check_main.html')

def student_register(request):
    students = User.objects.filter(is_staff=False)
    teachers = User.objects.filter(is_staff=True)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student_register_instance = form.save(commit=False)
            # 월요일
            student_register_instance.mon8 = form.cleaned_data['mon8']
            student_register_instance.mon9 = form.cleaned_data['mon9']
            student_register_instance.mon10 = form.cleaned_data['mon10']
            student_register_instance.mon11 = form.cleaned_data['mon11']
            student_register_instance.mon12 = form.cleaned_data['mon12']
            student_register_instance.mon13 = form.cleaned_data['mon13']
            student_register_instance.mon14 = form.cleaned_data['mon14']
            student_register_instance.mon15 = form.cleaned_data['mon15']
            student_register_instance.mon16 = form.cleaned_data['mon16']
            student_register_instance.mon17 = form.cleaned_data['mon17']
            student_register_instance.mon18 = form.cleaned_data['mon18']
            student_register_instance.mon19 = form.cleaned_data['mon19']
            student_register_instance.mon20 = form.cleaned_data['mon20']
            student_register_instance.mon21 = form.cleaned_data['mon21']
            student_register_instance.mon22 = form.cleaned_data['mon22']
            # 화요일
            student_register_instance.tue8 = form.cleaned_data['tue8']
            student_register_instance.tue9 = form.cleaned_data['tue9']
            student_register_instance.tue10 = form.cleaned_data['tue10']
            student_register_instance.tue11 = form.cleaned_data['tue11']
            student_register_instance.tue12 = form.cleaned_data['tue12']
            student_register_instance.tue13 = form.cleaned_data['tue13']
            student_register_instance.tue14 = form.cleaned_data['tue14']
            student_register_instance.tue15 = form.cleaned_data['tue15']
            student_register_instance.tue16 = form.cleaned_data['tue16']
            student_register_instance.tue17 = form.cleaned_data['tue17']
            student_register_instance.tue18 = form.cleaned_data['tue18']
            student_register_instance.tue19 = form.cleaned_data['tue19']
            student_register_instance.tue20 = form.cleaned_data['tue20']
            student_register_instance.tue21 = form.cleaned_data['tue21']
            student_register_instance.tue22 = form.cleaned_data['tue22']
            # 수요일
            student_register_instance.wed8 = form.cleaned_data['wed8']
            student_register_instance.wed9 = form.cleaned_data['wed9']
            student_register_instance.wed10 = form.cleaned_data['wed10']
            student_register_instance.wed11 = form.cleaned_data['wed11']
            student_register_instance.wed12 = form.cleaned_data['wed12']
            student_register_instance.wed13 = form.cleaned_data['wed13']
            student_register_instance.wed14 = form.cleaned_data['wed14']
            student_register_instance.wed15 = form.cleaned_data['wed15']
            student_register_instance.wed16 = form.cleaned_data['wed16']
            student_register_instance.wed17 = form.cleaned_data['wed17']
            student_register_instance.wed18 = form.cleaned_data['wed18']
            student_register_instance.wed19 = form.cleaned_data['wed19']
            student_register_instance.wed20 = form.cleaned_data['wed20']
            student_register_instance.wed21 = form.cleaned_data['wed21']
            student_register_instance.wed22 = form.cleaned_data['wed22']
            # 목요일
            student_register_instance.thu8 = form.cleaned_data['thu8']
            student_register_instance.thu9 = form.cleaned_data['thu9']
            student_register_instance.thu10 = form.cleaned_data['thu10']
            student_register_instance.thu11 = form.cleaned_data['thu11']
            student_register_instance.thu12 = form.cleaned_data['thu12']
            student_register_instance.thu13 = form.cleaned_data['thu13']
            student_register_instance.thu14 = form.cleaned_data['thu14']
            student_register_instance.thu15 = form.cleaned_data['thu15']
            student_register_instance.thu16 = form.cleaned_data['thu16']
            student_register_instance.thu17 = form.cleaned_data['thu17']
            student_register_instance.thu18 = form.cleaned_data['thu18']
            student_register_instance.thu19 = form.cleaned_data['thu19']
            student_register_instance.thu20 = form.cleaned_data['thu20']
            student_register_instance.thu21 = form.cleaned_data['thu21']
            student_register_instance.thu22 = form.cleaned_data['thu22']
            # 금요일
            student_register_instance.fri8 = form.cleaned_data['fri8']
            student_register_instance.fri9 = form.cleaned_data['fri9']
            student_register_instance.fri10 = form.cleaned_data['fri10']
            student_register_instance.fri11 = form.cleaned_data['fri11']
            student_register_instance.fri12 = form.cleaned_data['fri12']
            student_register_instance.fri13 = form.cleaned_data['fri13']
            student_register_instance.fri14 = form.cleaned_data['fri14']
            student_register_instance.fri15 = form.cleaned_data['fri15']
            student_register_instance.fri16 = form.cleaned_data['fri16']
            student_register_instance.fri17 = form.cleaned_data['fri17']
            student_register_instance.fri18 = form.cleaned_data['fri18']
            student_register_instance.fri19 = form.cleaned_data['fri19']
            student_register_instance.fri20 = form.cleaned_data['fri20']
            student_register_instance.fri21 = form.cleaned_data['fri21']
            student_register_instance.fri22 = form.cleaned_data['fri22']
            # 토요일
            student_register_instance.sat8 = form.cleaned_data['sat8']
            student_register_instance.sat9 = form.cleaned_data['sat9']
            student_register_instance.sat10 = form.cleaned_data['sat10']
            student_register_instance.sat11 = form.cleaned_data['sat11']
            student_register_instance.sat12 = form.cleaned_data['sat12']
            student_register_instance.sat13 = form.cleaned_data['sat13']
            student_register_instance.sat14 = form.cleaned_data['sat14']
            student_register_instance.sat15 = form.cleaned_data['sat15']
            student_register_instance.sat16 = form.cleaned_data['sat16']
            student_register_instance.sat17 = form.cleaned_data['sat17']
            student_register_instance.sat18 = form.cleaned_data['sat18']
            student_register_instance.sat19 = form.cleaned_data['sat19']
            student_register_instance.sat20 = form.cleaned_data['sat20']
            student_register_instance.sat21 = form.cleaned_data['sat21']
            student_register_instance.sat22 = form.cleaned_data['sat22']
            # 일요일
            student_register_instance.sun8 = form.cleaned_data['sun8']
            student_register_instance.sun9 = form.cleaned_data['sun9']
            student_register_instance.sun10 = form.cleaned_data['sun10']
            student_register_instance.sun11 = form.cleaned_data['sun11']
            student_register_instance.sun12 = form.cleaned_data['sun12']
            student_register_instance.sun13 = form.cleaned_data['sun13']
            student_register_instance.sun14 = form.cleaned_data['sun14']
            student_register_instance.sun15 = form.cleaned_data['sun15']
            student_register_instance.sun16 = form.cleaned_data['sun16']
            student_register_instance.sun17 = form.cleaned_data['sun17']
            student_register_instance.sun18 = form.cleaned_data['sun18']
            student_register_instance.sun19 = form.cleaned_data['sun19']
            student_register_instance.sun20 = form.cleaned_data['sun20']
            student_register_instance.sun21 = form.cleaned_data['sun21']
            student_register_instance.sun22 = form.cleaned_data['sun22']

            form.save()
            return redirect('check:index')
    else:
        form = StudentRegisterForm()
    context = {'teachers': teachers, 'students': students, 'form': form}

    return render(request, 'check/student_register_form.html', context)
