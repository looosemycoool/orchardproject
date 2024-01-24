from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from check.models import StudentRegister
from manager.models import ConsultingReport
# from reserve.models import Reserve

def index(request):
    students_p = StudentRegister.objects.filter(class_name='P').order_by('class_num')
    students_s = StudentRegister.objects.filter(class_name='S').order_by('class_num')
    students_m = StudentRegister.objects.filter(class_name='M').order_by('class_num')

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
    return render(request, 'report/consulting/consulting_main.html', context)

def consulting_report(request, student_id):
    consulting_data = ConsultingReport.objects.filter(student_id=student_id).order_by('-id')
    weekly_reports = []

    for data in consulting_data:
        week_report = {}

        week_report['month'] = data.month
        week_report['student_name'] = data.student.student
        week_report['content'] = {
            'subject_consulting': data.subject_consulting,
            'study_review': data.study_review,
        }

        weekly_reports.append(week_report)

    context = {'weekly_reports': weekly_reports}
    return render(request, 'report/consulting/consulting_report.html', context)
