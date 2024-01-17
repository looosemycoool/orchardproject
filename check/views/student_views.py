from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from ..models import Attendance, StudentRegister
from ..forms import StudentRegisterForm

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def index(request):
    students_p = StudentRegister.objects.filter(class_name='P', is_dropped=False).order_by('class_num')
    students_s = StudentRegister.objects.filter(class_name='S', is_dropped=False).order_by('class_num')
    students_m = StudentRegister.objects.filter(class_name='M', is_dropped=False).order_by('class_num')

    p_line1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
    p_line2 = ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    s_line1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    s_line2 = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
    s_line3 = ['41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60']

    context = {'students_p': students_p, 'students_s': students_s, 'students_m': students_m, 'p_line1': p_line1, 'p_line2': p_line2, 's_line1': s_line1, 's_line2': s_line2, 's_line3': s_line3}
    return render(request, 'check/student/student_main.html', context)

def register(request):
    students = User.objects.filter(is_staff=False).order_by('first_name')
    teachers = User.objects.filter(is_staff=True)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student_register_instance = form.save(commit=False)
            student_register_instance.drop_date = form.cleaned_data['drop_date']
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
            return redirect('check:student')
    else:
        form = StudentRegisterForm()
    context = {'teachers': teachers, 'students': students, 'form': form}

    return render(request, 'check/student/student_register_form.html', context)

def modify(request, student_id):
    students = User.objects.filter(is_staff=False).order_by('first_name')
    teachers = User.objects.filter(is_staff=True)

    student = get_object_or_404(StudentRegister, id=student_id)

    if request.method == 'POST':
        form = StudentRegisterForm(request.POST, instance=student)
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

            student_register_instance.save()

            return redirect('check:student')
    else:
        form = StudentRegisterForm(instance=student)

    context = {'form': form, 'students': students, 'student': student, 'teachers': teachers}
    return render(request, 'check/student/student_register_form.html', context)