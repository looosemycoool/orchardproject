from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ..models import Student_Study_Data
from django.conf import settings

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1eWqyXWJSRPaEyEjOHn-pvZarSuQep2T93Rs96TU4z7U/edit#gid=1019871936"

# student_tod
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
                korean_self_study=(int(item[4] or 0)) * 60 + (int(item[5] or 0)),
                korean_lecture_study=(int(item[6] or 0)) * 60 + (int(item[7] or 0)),
                math_self_study=(int(item[8] or 0)) * 60 + (int(item[9] or 0)),
                math_lecture_study=(int(item[10] or 0)) * 60 + (int(item[11] or 0)),
                english_self_study=(int(item[12] or 0)) * 60 + (int(item[13] or 0)),
                english_lecture_study=(int(item[14] or 0)) * 60 + (int(item[15] or 0)),
                research1_self_study=(int(item[16] or 0)) * 60 + (int(item[17] or 0)),
                research1_lecture_study=(int(item[18] or 0)) * 60 + (int(item[19] or 0)),
                research2_self_study=(int(item[20] or 0)) * 60 + (int(item[21] or 0)),
                research2_lecture_study=(int(item[22] or 0)) * 60 + (int(item[23] or 0)),
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


# return render(request, 'manager/student_study/student_study_main.html')


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
