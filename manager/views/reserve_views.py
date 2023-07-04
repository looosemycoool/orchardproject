from django.shortcuts import render, redirect
from reserve.models import Teacher, Time_Table, Reserve
# from ..forms import ReserveForm, Reserve_Create_Form
# from datetime import datetime, timedelta

def reserve(request):
    return render(request, 'manager/reserve/manager_reserve_main.html')
def reserve_create(request):
    return render(request, 'manager/reserve/manager_reserve_create.html')

# def reserve_create(request):
#     if request.method == 'GET':
#         form = Reserve_Create_Form(request.GET)
#
#     if request.method == 'POST':
#         form = ReserveForm(request.POST)
#         if form.is_valid():
#             teacher = form.cleaned_data['teacher']
#             date = form.cleaned_data['date']
#             start_time = form.cleaned_data['start_time']
#             end_time = form.cleaned_data['end_time']
#
#             # Time_Table에서 시작 시간과 끝나는 시간을 가져옴
#             time_table = Time_Table.objects.filter(time__gte=start_time, time__lte=end_time)
#
#             # 선택된 시작 시간부터 끝나는 시간까지 20분 간격으로 Reserve 객체 생성
#             current_time = datetime.combine(date, start_time)
#             end_datetime = datetime.combine(date, end_time)
#             while current_time <= end_datetime:
#                 Reserve.objects.create(
#                     teacher_id=teacher,
#                     date=date,
#                     time=current_time.time(),
#                     student_name=request.user
#                 )
#                 current_time += timedelta(minutes=20)
#
#             return redirect('manager:reserve_list')
#     else:
#         form = ReserveForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'manager/reserve_create.html', context)

def reserve_detail(request):
    return render(request, 'manager/reserve/manager_reserve_detail.html')