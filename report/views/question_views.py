from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from check.models import StudentRegister
from reserve.models import Reserve

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
    return render(request, 'report/question/question_main.html', context)

def question_report(request, student_id):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    student = StudentRegister.objects.get(id=student_id, is_dropped=False)

    question_data = Reserve.objects.filter(student_name__username=student.username, date__range=[start_date, end_date])

    subject_question_counts = {
        'korean': 0,
        'math': 0,
        'english': 0,
        'research': 0
    }
    subject_consulting_counts = {
        'korean': 0,
        'math': 0,
        'english': 0,
        'research': 0
    }

    for data in question_data:
        if data.subject in subject_question_counts and data.type == 'question':
            subject_question_counts[data.subject] += 1
        elif data.subject in ['chemistry', 'biology', 'physics', 'earth', 'science', 'social'] and data.type == 'question':
            subject_question_counts['research'] += 1

    for data in question_data:
        if data.subject in subject_consulting_counts and (data.type == 'new_counseling' or data.type == 'study_counseling'):
            subject_consulting_counts[data.subject] += 1
        elif data.subject in ['chemistry', 'biology', 'physics', 'earth', 'science', 'social'] and (data.type == 'new_counseling' or data.type == 'study_counseling'):
            subject_consulting_counts['research'] += 1

    report = {
        'start_date': start_date,
        'end_date': end_date,
        'question_counts': subject_question_counts,
        'consulting_counts': subject_consulting_counts
    }
    print(subject_question_counts['korean'])

    context = {'student': student, 'report': report}
    return render(request, 'report/question/question_report.html', context)
