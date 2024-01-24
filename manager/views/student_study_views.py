from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ..models import Student_Study_Data, Average_Study_Data
from check.models import StudentRegister
from ..forms import Student_Study_DataForm
from django.conf import settings
from collections import defaultdict

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1eWqyXWJSRPaEyEjOHn-pvZarSuQep2T93Rs96TU4z7U/edit#gid=1019871936"

def new_student_study(request):
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
    return render(request, 'manager/student_study/student_study_main.html', context)

def new_student_study_detail(request, student_id):
    data = Student_Study_Data.objects.filter(user__id=student_id).order_by('-id')
    student = StudentRegister.objects.filter(id=student_id) # 단일 객체를 가져오기
    research1 = student.values('research1_select')[0]['research1_select']
    research2 = student.values('research2_select')[0]['research2_select']
    # research3 = student.values('research3_select')[0]['research3_select']

    selected_week = request.GET.get('selected_week')

    if selected_week:
        filtered_data = Student_Study_Data.objects.filter(week_name=selected_week, user__id=student_id)
        total_study = filtered_data[0].korean_study + filtered_data[0].math_study + filtered_data[0].english_study + filtered_data[0].research1_study + filtered_data[0].research2_study
        total_self_study = filtered_data[0].korean_self_study + filtered_data[0].math_self_study + filtered_data[0].english_self_study + filtered_data[0].research1_self_study + filtered_data[0].research2_self_study
    else:
        filtered_data = []
        total_study = 0
        total_self_study = 0

    print(student)
    context = {
        'data': data,
        'student': student,
        'research1': research1,
        'research2': research2,
        'selected_week': selected_week,
        'filtered_data': filtered_data,
        'total_study': total_study,
        'total_self_study': total_self_study
    }
    return render(request, 'manager/student_study/student_study_detail.html', context)

def planner_create(request, student_id):
    student = StudentRegister.objects.get(id=student_id)  # 단일 객체 가져오기
    data = Student_Study_Data.objects.filter(user__id=student_id).order_by('-id')

    if request.method == 'POST':
        form = Student_Study_DataForm(request.POST)
        if form.is_valid():
            week_name = form.cleaned_data['week_name']
            # 중복 검사
            if Student_Study_Data.objects.filter(user=student, week_name=week_name).exists():
                form.add_error('week_name', ValidationError(_("이미 등록된 기간입니다.")))
                context = {'student': student, 'form': form, 'data': data}
                return render(request, 'manager/student_study/student_study_form.html', context)

            study_data = form.save(commit=False)
            study_data.week_name = form.cleaned_data['week_name']
            # study_data.student_name = student
            study_data.user = student
            study_data.korean_study = form.cleaned_data['korean_study']
            study_data.korean_self_study = form.cleaned_data['korean_self_study']

            study_data.math_study = form.cleaned_data['math_study']
            study_data.math_self_study = form.cleaned_data['math_self_study']

            study_data.english_study = form.cleaned_data['english_study']
            study_data.english_self_study = form.cleaned_data['english_self_study']

            study_data.research1_study = form.cleaned_data['research1_study']
            study_data.research1_self_study = form.cleaned_data['research1_self_study']

            # study_data.research2_study = form.cleaned_data['research2_study']
            # study_data.research2_self_study = form.cleaned_data['research2_self_study']
            #
            # study_data.research3_study = form.cleaned_data['research3_study']
            # study_data.research3_self_study = form.cleaned_data['research3_self_study']
            study_data.save()  # 데이터 저장
            student_id = student.id
            return redirect('manager:student_study_detail', student_id=student_id)
    else:
        form = Student_Study_DataForm()

    context = {'student': student, 'form': form, 'data': data}
    return render(request, 'manager/student_study/student_study_form.html', context)

def planner_modify(request, data_id):
    week_data = get_object_or_404(Student_Study_Data, id=data_id)  # 단일 객체 가져오기
    data = Student_Study_Data.objects.filter(user__id=week_data.user_id).order_by('-id')

    student = get_object_or_404(StudentRegister, id=week_data.user_id)
    student_id = student.id

    if request.method == 'POST':
        form = Student_Study_DataForm(request.POST, instance=week_data)
        # if form.is_valid():
        #     study_data = form.save(commit=False)
        #     study_data.user = student.id
        #     # 필요한 경우 study_data의 추가 필드를 업데이트
        #     study_data.save()  # 데이터 저장
        #     student_id = student.id
        #     return redirect('manager:student_study_detail', student_id=student_id)
        if form.is_valid():
            study_data = form.save(commit=False)
            # student_id = form.cleaned_data.get('user')  # 또는 week_data.user_id 등을 사용
            study_data.user = StudentRegister.objects.get(id=student_id)  # StudentRegister 인스턴스를 할당
            # study_data.student_name = week_data.student_name
            study_data.save()
            return redirect('manager:student_study_detail', student_id=student_id)

    else:
        form = Student_Study_DataForm(instance=week_data)

    context = {'form': form, 'data': data, 'student': student, 'week_data': week_data}
    return render(request, 'manager/student_study/student_study_form.html', context)

def planner_delete(request, data_id):
    week_data = get_object_or_404(Student_Study_Data, id=data_id)
    student_id = week_data.user_id
    week_data.delete()
    return redirect('manager:student_study_detail', student_id=student_id)

def student_study(request):
    if request.method == 'POST':
        sheet_name = request.POST.get('sheet_name')

        scope = "https://spreadsheets.google.com/feeds"
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(
            settings.GOOGLE_SHEETS_CREDENTIALS, scope)
        gc = gspread.authorize(credentials)

        # URL을 이용하여 시트 불러오기
        doc = gc.open_by_url(spreadsheet_url)

        # 시트에서 데이터 가져오기
        worksheet = doc.worksheet(sheet_name)
        data = worksheet.get_all_values()[1:]

        result = {}

        subject_study_time = defaultdict(int)  # 각 과목별 자습 시간을 누적하기 위한 딕셔너리
        subject_student_count = defaultdict(int)  # 각 과목별 학생 수를 계산하기 위한 딕셔너리

        for item in data:
            if item[1] == "":
                continue
            # 누적 자습 시간 계산
            subject_study_time['korean_lecture_study'] += (int(item[4] or 0)) * 60 + (int(item[5] or 0))
            subject_study_time['korean_self_study'] += (int(item[6] or 0)) * 60 + (int(item[7] or 0))
            subject_study_time['math_lecture_study'] += (int(item[8] or 0)) * 60 + (int(item[9] or 0))
            subject_study_time['math_self_study'] += (int(item[10] or 0)) * 60 + (int(item[11] or 0))
            subject_study_time['english_lecture_study'] += (int(item[12] or 0)) * 60 + (int(item[13] or 0))
            subject_study_time['english_self_study'] += (int(item[14] or 0)) * 60 + (int(item[15] or 0))
            subject_study_time['research_lecture_study'] += (int(item[16] or 0)) * 60 + (int(item[17] or 0)) + (
                int(item[20] or 0)) * 60 + (int(item[21] or 0))
            subject_study_time['research_self_study'] += (int(item[18] or 0)) * 60 + (int(item[19] or 0)) + (
                int(item[22] or 0)) * 60 + (int(item[23] or 0))

            subject_study_time['total_lecture_study'] += (int(item[4] or 0)) * 60 + (int(item[5] or 0)) + (
                int(item[8] or 0)) * 60 + (int(item[9] or 0)) + (int(item[12] or 0)) * 60 + (int(item[13] or 0)) + (
                                                             int(item[16] or 0)) * 60 + (int(item[17] or 0)) + (
                                                             int(item[20] or 0)) * 60 + (int(item[21] or 0))
            subject_study_time['total_self_study'] += (int(item[6] or 0)) * 60 + (int(item[7] or 0)) + (
                int(item[10] or 0)) * 60 + (int(item[11] or 0)) + (int(item[14] or 0)) * 60 + (int(item[15] or 0)) + (
                                                          int(item[18] or 0)) * 60 + (int(item[19] or 0)) + (
                                                          int(item[22] or 0)) * 60 + (int(item[23] or 0))

            subject_study_time['total_study'] += (int(item[4] or 0)) * 60 + (int(item[5] or 0)) + (
                int(item[8] or 0)) * 60 + (int(item[9] or 0)) + (int(item[12] or 0)) * 60 + (int(item[13] or 0)) + (
                                                     int(item[16] or 0)) * 60 + (int(item[17] or 0)) + (
                                                     int(item[20] or 0)) * 60 + (int(item[21] or 0)) + (
                                                     int(item[6] or 0)) * 60 + (int(item[7] or 0)) + (
                                                     int(item[10] or 0)) * 60 + (int(item[11] or 0)) + (
                                                     int(item[14] or 0)) * 60 + (int(item[15] or 0)) + (
                                                     int(item[18] or 0)) * 60 + (int(item[19] or 0)) + (
                                                     int(item[22] or 0)) * 60 + (int(item[23] or 0))

            # 학생 수 계산
            subject_student_count['korean_lecture_study'] += int(bool(item[4] or item[5]))
            subject_student_count['korean_self_study'] += int(bool(item[6] or item[7]))
            subject_student_count['math_lecture_study'] += int(bool(item[8] or item[9]))
            subject_student_count['math_self_study'] += int(bool(item[10] or item[11]))
            subject_student_count['english_lecture_study'] += int(bool(item[12] or item[13]))
            subject_student_count['english_self_study'] += int(bool(item[14] or item[15]))
            subject_student_count['research_lecture_study'] += int(bool(item[16] or item[17] or item[20] or item[21]))
            subject_student_count['research_self_study'] += int(bool(item[18] or item[19] or item[22] or item[23]))

            subject_student_count['total_self_study'] += int(bool(
                item[6] or item[7] or item[10] or item[11] or item[14] or item[15] or item[18] or item[19] or item[
                    22] or item[23]))
            subject_student_count['total_lecture_study'] += int(bool(
                item[4] or item[5] or item[8] or item[9] or item[12] or item[13] or item[16] or item[17] or item[20] or
                item[22]))

            subject_student_count['total_study'] += int(bool(
                item[6] or item[7] or item[10] or item[11] or item[14] or item[15] or item[18] or item[19] or item[
                    22] or item[23] or item[4] or item[5] or item[8] or item[9] or item[12] or item[13] or item[16] or
                item[17] or item[20] or item[22]))

        # 과목별 평균 자습 시간 계산
        average_study_time = {subject: int(study_time / max(student_count, 1)) for subject, study_time, student_count in
                              zip(
                                  subject_study_time.keys(), subject_study_time.values(), subject_student_count.values()
                              )}

        # 결과 저장
        average_study_data = Average_Study_Data(
            week_name=sheet_name,
            korean_lecture_study_average=average_study_time['korean_lecture_study'],
            korean_self_study_average=average_study_time['korean_self_study'],
            math_lecture_study_average=average_study_time['math_lecture_study'],
            math_self_study_average=average_study_time['math_self_study'],
            english_lecture_study_average=average_study_time['english_lecture_study'],
            english_self_study_average=average_study_time['english_self_study'],
            research_lecture_study_average=average_study_time['research_lecture_study'],
            research_self_study_average=average_study_time['research_self_study'],

            total_lecture_study_average=average_study_time['total_lecture_study'],
            total_self_study_average=average_study_time['total_self_study'],

            total_study_average=average_study_time['total_study']
        )
        average_study_data.save()

        for item in data:
            if item[1] == "":
                continue
                # ss - self_study
                # il - internet_lecture
            student_name = item[1]
            research1 = item[2]
            research2 = item[3]
            # Check if the data already exists in the database
            existing_data = Student_Study_Data.objects.filter(week_name=sheet_name, student_name=student_name)
            if existing_data.exists():
                continue

            student_study_data = Student_Study_Data(
                week_name=sheet_name,
                student_name=student_name,
                research1=research1,
                research2=research2,
                korean_lecture_study=(int(item[4] or 0)) * 60 + (int(item[5] or 0)),
                korean_self_study=(int(item[6] or 0)) * 60 + (int(item[7] or 0)),
                math_lecture_study=(int(item[8] or 0)) * 60 + (int(item[9] or 0)),
                math_self_study=(int(item[10] or 0)) * 60 + (int(item[11] or 0)),
                english_lecture_study=(int(item[12] or 0)) * 60 + (int(item[13] or 0)),
                english_self_study=(int(item[14] or 0)) * 60 + (int(item[15] or 0)),
                research1_lecture_study=(int(item[16] or 0)) * 60 + (int(item[17] or 0)),
                research1_self_study=(int(item[18] or 0)) * 60 + (int(item[19] or 0)),
                research2_lecture_study=(int(item[20] or 0)) * 60 + (int(item[21] or 0)),
                research2_self_study=(int(item[22] or 0)) * 60 + (int(item[23] or 0)),
                total_study_time=(int(item[4] or 0)) * 60 + (int(item[5] or 0)) + (int(item[6] or 0)) * 60 + (
                    int(item[7] or 0)) + (int(item[8] or 0)) * 60 + (int(item[9] or 0)) + (int(item[10] or 0)) * 60 + (
                                     int(item[11] or 0)) + (int(item[12] or 0)) * 60 + (int(item[13] or 0)) + (
                                     int(item[14] or 0)) * 60 + (int(item[15] or 0)) + (int(item[16] or 0)) * 60 + (
                                     int(item[17] or 0)) + (int(item[18] or 0)) * 60 + (int(item[19] or 0)) + (
                                     int(item[20] or 0)) * 60 + (int(item[21] or 0)) + (int(item[22] or 0)) * 60 + (
                                     int(item[23] or 0))
            )
            result[student_name] = student_study_data

        # 모든 데이터를 저장한 후에 한 번에 저장합니다.
        for student_name, student_study_data in result.items():
            student_study_data.save()

        return redirect('manager:student_study_upload_success')

    if request.method == 'GET':
        student_name = request.GET.get('student_name')

        # Query the database based on the search parameters
        if student_name:
            queryset = Student_Study_Data.objects.filter(student_name__icontains=student_name).order_by('week_name')
        else:
            queryset = Student_Study_Data.objects.all().order_by('week_name')

        context = {'data_list': queryset}
        return render(request, 'manager/student_study/student_study_main.html', context)
    return render(request, 'manager/student_study/student_study_main.html')


def student_study_detail(request):
    student_name = request.GET.get('student_name')
    selected_week = request.GET.get('selected_week')

    if student_name:
        # Query the database to get the patrol data for the specified student
        student_study_data = Student_Study_Data.objects.filter(student_name__icontains=student_name).order_by(
            'week_name')

        # Extract unique dates for the student
        unique_week = student_study_data.values_list('week_name', flat=True).distinct()

        if selected_week:
            # Filter the data based on the selected date
            filtered_data = student_study_data.filter(week_name=selected_week)
        else:
            filtered_data = []

        context = {
            'student_name': student_name,
            'unique_week': unique_week,
            'selected_week': selected_week,
            'filtered_data': filtered_data,
        }
        return render(request, 'manager/student_study/student_study_detail.html', context)
    return render(request, 'manager/student_study/student_study_detail.html')


def student_study_upload_success(request):
    return render(request, 'manager/student_study/student_study_upload_success.html')


def student_study_upload_fail(request):
    return render(request, 'manager/student_study/student_study_upload_fail.html')