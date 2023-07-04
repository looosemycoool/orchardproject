from django.shortcuts import render, redirect
import gspread
from gspread.exceptions import WorksheetNotFound
from oauth2client.service_account import ServiceAccountCredentials
from ..models import Patrol_Data
from django.conf import settings

spreadsheet_url = "https://docs.google.com/spreadsheets/d/1PowGIq5w_2y7pSCeP0V4DG9oEEjAlqEVrmcQEqas098/edit#gid=733072548"

def patrol(request):
    # 업로드 과정
    if request.method == "POST":
        sheet_name = request.POST.get("sheet_name")

        scope = "https://spreadsheets.google.com/feeds"
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(
            settings.GOOGLE_SHEETS_CREDENTIALS, scope
        )
        gc = gspread.authorize(credentials)

        doc = gc.open_by_url(spreadsheet_url)
        try:
            worksheet = doc.worksheet(sheet_name)
            data = worksheet.get_all_values()[2:]

            result = {}

            for item in data:
                if item[1] == "":
                    continue
                # ss - self_study
                # il - internet_lecture
                student_name = item[1]

                # Check if the data already exists in the database
                existing_data = Patrol_Data.objects.filter(date=sheet_name, student_name=student_name)
                if existing_data.exists():
                    continue  # Skip if data already exists

                patrol_data = Patrol_Data(
                    date=sheet_name,
                    student_name=student_name,

                    k_ss_count=item.count("국어자습"),  # korean
                    k_il_count=item.count("국어인강"),
                    m_ss_count=item.count("수학자습"),  # math
                    m_il_count=item.count("수학인강"),
                    e_ss_count=item.count("영어자습"),  # english
                    e_il_count=item.count("영어인강"),
                    r_ss_count=item.count("탐구자습"),  # research
                    r_il_count=item.count("탐구인강"),
                    plan=item.count("계획정리"),
                    mentoring=item.count("멘토링"),
                    question=item.count("질의응답"),
                    consulting=item.count("상담"),
                    sleep=item.count("수면"),

                    focus_three=item.count('3'),
                    focus_two=item.count('2'),
                    focus_one=item.count('1'),
                    total_focus_count=item.count('3') + item.count('2') + item.count('1')
                )
                result[student_name] = patrol_data
            for student_name, patrol_data in result.items():
                patrol_data.save()

            return redirect("manager:patrol_upload_success")
        except WorksheetNotFound:
            error_message = f"Worksheet '{sheet_name}' not found. Please make sure the sheet exists."
            return render(request, 'manager/student_study/student_study_upload_fail.html',
                          {'error_message': error_message})
        # 검색 과정
    if request.method == 'GET':
        student_name = request.GET.get('student_name')

        # Query the database based on the search parameters
        if student_name:
            queryset = Patrol_Data.objects.filter(student_name__icontains=student_name).order_by('date')
        else:
            queryset = Patrol_Data.objects.all().order_by('date')

        context = {'data_list': queryset}
        return render(request, 'manager/patrol/patrol_main.html', context)
    return render(request, 'manager/patrol/patrol_main.html')

def patrol_student_detail(request):
    student_name = request.GET.get('student_name')
    selected_date = request.GET.get('selected_date')

    if student_name:
        # Query the database to get the patrol data for the specified student
        student_patrol_data = Patrol_Data.objects.filter(student_name__icontains=student_name).order_by('date')

        # Extract unique dates for the student
        unique_dates = student_patrol_data.values_list('date', flat=True).distinct()

        if selected_date:
            # Filter the data based on the selected date
            filtered_data = student_patrol_data.filter(date=selected_date)
        else:
            filtered_data = []

        context = {
            'student_name': student_name,
            'unique_dates': unique_dates,
            'selected_date': selected_date,
            'filtered_data': filtered_data,
        }
        return render(request, 'manager/patrol/patrol_student_detail.html', context)

    return render(request, 'manager/patrol/patrol_student_detail.html')


def patrol_upload_success(request):
    return render(request, 'manager/patrol/patrol_upload_success.html')

def patrol_upload_fail(request):
    return render(request, 'manager/patrol/patrol_upload_fail.html')
