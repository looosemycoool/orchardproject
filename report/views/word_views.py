from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from check.models import StudentRegister
from manager.models import WordTest
from reserve.models import Reserve

def index(request):
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
    return render(request, 'report/word/word_main.html', context)

def word_report(request, student_id):
    word_month = request.GET.get('word_month')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    student = StudentRegister.objects.get(id=student_id, is_dropped=False)
    months = WordTest.objects.filter(student_id=student.id).values('month').order_by('-id')

    word_data = WordTest.objects.filter(student_id=student.id, month=word_month)

    report = {
        'start_date': start_date,
        'end_date': end_date,
    }

    context = {'student': student, 'report': report, 'months': months, 'word_data': word_data}
    return render(request, 'report/word/word_report.html', context)
