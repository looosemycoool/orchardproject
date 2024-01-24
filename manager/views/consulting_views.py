from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from ..models import ConsultingReport
from check.models import StudentRegister
from ..forms import ConsultingReportForm
def index(request):
    # students = StudentRegister.objects.filter(is_dropped=False)
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

    return render(request, 'manager/consulting/consulting_main.html', context)

def consulting_detail(request, student_id):
    data = ConsultingReport.objects.filter(student__id=student_id).order_by('-id')
    student = StudentRegister.objects.filter(id=student_id)  # 단일 객체를 가져오기

    months = data.values('month').distinct()

    select_month = request.GET.get('select_month')

    if select_month:
        filtered_data = ConsultingReport.objects.filter(month=select_month, student_id=student_id)
    else:
        filtered_data = []

    context = {
        'data': data,
        'student': student,
        'months': months,
        'select_month': select_month,
        'filtered_data': filtered_data,
    }
    return render(request, 'manager/consulting/consulting_detail.html', context)

def consulting_create(request, student_id):
    student = StudentRegister.objects.get(id=student_id)
    data = ConsultingReport.objects.filter(student__id=student_id).order_by('-id')
    if request.method == 'POST':
        form = ConsultingReportForm(request.POST)
        if form.is_valid():
            consulting_data = form.save(commit=False)
            consulting_data.student = student
            consulting_data.save()
            return redirect('manager:consulting_detail', student_id)
    else:
        form = ConsultingReportForm()
    context = {'form': form, 'student': student, 'data': data}
    return render(request, 'manager/consulting/consulting_form.html', context)

def consulting_modify(request, data_id):
    month_data = get_object_or_404(ConsultingReport, pk=data_id)
    data = ConsultingReport.objects.filter(student=month_data.student).order_by('-id')

    student = get_object_or_404(StudentRegister, id=month_data.student_id)
    student_id = student.id

    if request.method == "POST":
        form = ConsultingReportForm(request.POST, instance=month_data)
        if form.is_valid():
            consulting_data = form.save(commit=False)
            consulting_data.student = StudentRegister.objects.get(id=student_id)
            consulting_data.save()
            return redirect('manager:consulting_detail', student_id=student_id)
    else:
        form = ConsultingReportForm(instance=month_data)
    context = {'form': form, 'data': data, 'student': student, 'month_data': month_data}
    return render(request, 'manager/consulting/consulting_form.html', context)
def consulting_delete(request, data_id):
    data = get_object_or_404(ConsultingReport, id=data_id)
    student_id = data.student_id
    data.delete()
    return redirect('manager:consulting_detail', student_id=student_id)