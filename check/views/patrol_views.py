# from django.shortcuts import render, redirect, get_object_or_404
# from datetime import datetime
# from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import user_passes_test
# from ..models import StudentRegister
#
# @user_passes_test(lambda u: u.is_staff, login_url='common:login')
# def index(request):
#     return render(request, 'check/patrol_main.html')
#
# @user_passes_test(lambda u: u.is_staff, login_url='common:login')
# def patrol(request):
#     # patrol 페이지 목록 보여주기
#     return render(request, 'check/patrol_main.html')
#
# def get_day_of_week(selected_date):
#     date_object = datetime.strptime(selected_date, "%Y-%m-%d").date()
#     return date_object.strftime("%a")
#
# def create_patrol_book(request):
#     if request.method == 'POST':
#         selected_date = request.POST.get('selected_date', None)
#         day_of_week = get_day_of_week(selected_date)
#
#         # 8부터 22까지의 시간대에 해당하는 필드가 비어 있지 않은 경우를 확인
#         time_fields = [f"{day_of_week.lower()}{hour}" for hour in range(8, 23)]
#         filter_params = {f"{field}__isnull": False for field in time_fields}
#
#         students = StudentRegister.objects.filter(**filter_params, is_dropped=False)
#
#         for student in students:
#             if not PatrolCheck.objects.filter(user=student, date=selected_date).exists():
#                 create_patrol(request, student.id, selected_date)
#     return render(request, 'check/patrol_main.html')
#
# def create_patrol(request, student_register_id, selected_date):
#     student_register = StudentRegister.objects.get(pk=student_register_id)
#     day_of_week = datetime.strptime(selected_date, '%Y-%m-%d').strftime('%a').lower()
#
#     patrol_check_instance = PatrolCheck(user=student_register, date=selected_date, day_of_week=day_of_week)
#
#     patrol_check_instance.save()
#
#     return render(request, 'check/patrol_main.html')
#
# def patrol_p_class(request):
#     current_date = datetime.now().date()
#     patrol_p = PatrolCheck.objects.filter(user__class_name='P', date=current_date, user__is_dropped=False).order_by('user__class_num')
#
#     line1 = ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
#     line2 = ['41', '42', '43', '44', '45', '46', '47', '48', '49']
#     line3 = ['31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
#     line4 = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
#     line5 = ['12', '13', '14', '15', '16', '17', '18', '19', '20']
#     line6 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
#
#     context = {'patrol_p': patrol_p, 'line1': line1, 'line2': line2, 'line3': line3, 'line4': line4, 'line5':line5, 'line6':line6}
#     return render(request, 'check/patrol_p_class.html', context)
#
# def patrol_check_p(request, patrol_id):
#     patrol = PatrolCheck.objects.get(id=patrol_id)
#     if request.method == 'POST':
#         # 여기서 'time1_study'와 같은 필드를 request.POST에서 직접 처리합니다.
#         patrol.time1_study = request.POST.get(f'time1_study{patrol_id}', '')
#         patrol.time1_focus = request.POST.get(f'time1_focus{patrol_id}', '')
#
#         patrol.time2_study = request.POST.get(f'time2_study{patrol_id}', '')
#         patrol.time2_focus = request.POST.get(f'time2_focus{patrol_id}', '')
#
#         patrol.time3_study = request.POST.get(f'time3_study{patrol_id}', '')
#         patrol.time3_focus = request.POST.get(f'time3_focus{patrol_id}', '')
#
#         patrol.time4_study = request.POST.get(f'time4_study{patrol_id}', '')
#         patrol.time4_focus = request.POST.get(f'time4_focus{patrol_id}', '')
#
#         patrol.time5_study = request.POST.get(f'time5_study{patrol_id}', '')
#         patrol.time5_focus = request.POST.get(f'time5_focus{patrol_id}', '')
#
#         patrol.time6_study = request.POST.get(f'time6_study{patrol_id}', '')
#         patrol.time6_focus = request.POST.get(f'time6_focus{patrol_id}', '')
#
#         patrol.time7_study = request.POST.get(f'time7_study{patrol_id}', '')
#         patrol.time7_focus = request.POST.get(f'time7_focus{patrol_id}', '')
#
#         patrol.time8_study = request.POST.get(f'time8_study{patrol_id}', '')
#         patrol.time8_focus = request.POST.get(f'time8_focus{patrol_id}', '')
#
#         patrol.time9_study = request.POST.get(f'time9_study{patrol_id}', '')
#         patrol.time9_focus = request.POST.get(f'time9_focus{patrol_id}', '')
#
#         patrol.time10_study = request.POST.get(f'time10_study{patrol_id}', '')
#         patrol.time10_focus = request.POST.get(f'time10_focus{patrol_id}', '')
#
#         patrol.time11_study = request.POST.get(f'time11_study{patrol_id}', '')
#         patrol.time11_focus = request.POST.get(f'time11_focus{patrol_id}', '')
#
#         patrol.time12_study = request.POST.get(f'time12_study{patrol_id}', '')
#         patrol.time12_focus = request.POST.get(f'time12_focus{patrol_id}', '')
#
#         patrol.time13_study = request.POST.get(f'time13_study{patrol_id}', '')
#         patrol.time13_focus = request.POST.get(f'time13_focus{patrol_id}', '')
#
#         patrol.time14_study = request.POST.get(f'time14_study{patrol_id}', '')
#         patrol.time14_focus = request.POST.get(f'time14_focus{patrol_id}', '')
#
#         patrol.time15_study = request.POST.get(f'time15_study{patrol_id}', '')
#         patrol.time15_focus = request.POST.get(f'time15_focus{patrol_id}', '')
#
#         patrol.time16_study = request.POST.get(f'time16_study{patrol_id}', '')
#         patrol.time16_focus = request.POST.get(f'time16_focus{patrol_id}', '')
#
#         patrol.time17_study = request.POST.get(f'time17_study{patrol_id}', '')
#         patrol.time17_focus = request.POST.get(f'time17_focus{patrol_id}', '')
#
#         patrol.time18_study = request.POST.get(f'time18_study{patrol_id}', '')
#         patrol.time18_focus = request.POST.get(f'time18_focus{patrol_id}', '')
#
#         patrol.save()
#         return redirect('check:patrol_p_class')
#     return redirect('check:patrol_p_class')
#
#
# def patrol_s_class(request):
#     current_date = datetime.now().date()
#     patrol_s = PatrolCheck.objects.filter(user__class_name='S', date=current_date, user__is_dropped=False).order_by('user__class_num')
#     patrol_m = PatrolCheck.objects.filter(user__class_name='M', date=current_date, user__is_dropped=False).order_by('user__class_num')
#
#     line1 = ['24', '25', '26', '27', '28', '29', '30']
#     line2 = ['16', '17', '18', '19', '20', '21', '22', '23']
#     line3 = ['9', '10', '11', '12', '13', '14', '15']
#     line4 = ['1', '2', '3', '4', '5', '6', '7', '8']
#     line5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
#     context = {'patrol_s': patrol_s, 'line1': line1, 'line2': line2, 'line3': line3, 'line4': line4}
#     return render(request, 'check/patrol_s_class.html', context)
#
# def patrol_check_s(request, patrol_id):
#     patrol = PatrolCheck.objects.get(id=patrol_id)
#     if request.method == 'POST':
#         # 여기서 'time1_study'와 같은 필드를 request.POST에서 직접 처리합니다.
#         patrol.time1_study = request.POST.get(f'time1_study{patrol_id}', '')
#         patrol.time1_focus = request.POST.get(f'time1_focus{patrol_id}', '')
#
#         patrol.time2_study = request.POST.get(f'time2_study{patrol_id}', '')
#         patrol.time2_focus = request.POST.get(f'time2_focus{patrol_id}', '')
#
#         patrol.time3_study = request.POST.get(f'time3_study{patrol_id}', '')
#         patrol.time3_focus = request.POST.get(f'time3_focus{patrol_id}', '')
#
#         patrol.time4_study = request.POST.get(f'time4_study{patrol_id}', '')
#         patrol.time4_focus = request.POST.get(f'time4_focus{patrol_id}', '')
#
#         patrol.time5_study = request.POST.get(f'time5_study{patrol_id}', '')
#         patrol.time5_focus = request.POST.get(f'time5_focus{patrol_id}', '')
#
#         patrol.time6_study = request.POST.get(f'time6_study{patrol_id}', '')
#         patrol.time6_focus = request.POST.get(f'time6_focus{patrol_id}', '')
#
#         patrol.time7_study = request.POST.get(f'time7_study{patrol_id}', '')
#         patrol.time7_focus = request.POST.get(f'time7_focus{patrol_id}', '')
#
#         patrol.time8_study = request.POST.get(f'time8_study{patrol_id}', '')
#         patrol.time8_focus = request.POST.get(f'time8_focus{patrol_id}', '')
#
#         patrol.time9_study = request.POST.get(f'time9_study{patrol_id}', '')
#         patrol.time9_focus = request.POST.get(f'time9_focus{patrol_id}', '')
#
#         patrol.time10_study = request.POST.get(f'time10_study{patrol_id}', '')
#         patrol.time10_focus = request.POST.get(f'time10_focus{patrol_id}', '')
#
#         patrol.time11_study = request.POST.get(f'time11_study{patrol_id}', '')
#         patrol.time11_focus = request.POST.get(f'time11_focus{patrol_id}', '')
#
#         patrol.time12_study = request.POST.get(f'time12_study{patrol_id}', '')
#         patrol.time12_focus = request.POST.get(f'time12_focus{patrol_id}', '')
#
#         patrol.time13_study = request.POST.get(f'time13_study{patrol_id}', '')
#         patrol.time13_focus = request.POST.get(f'time13_focus{patrol_id}', '')
#
#         patrol.time14_study = request.POST.get(f'time14_study{patrol_id}', '')
#         patrol.time14_focus = request.POST.get(f'time14_focus{patrol_id}', '')
#
#         patrol.time15_study = request.POST.get(f'time15_study{patrol_id}', '')
#         patrol.time15_focus = request.POST.get(f'time15_focus{patrol_id}', '')
#
#         patrol.time16_study = request.POST.get(f'time16_study{patrol_id}', '')
#         patrol.time16_focus = request.POST.get(f'time16_focus{patrol_id}', '')
#
#         patrol.time17_study = request.POST.get(f'time17_study{patrol_id}', '')
#         patrol.time17_focus = request.POST.get(f'time17_focus{patrol_id}', '')
#
#         patrol.time18_study = request.POST.get(f'time18_study{patrol_id}', '')
#         patrol.time18_focus = request.POST.get(f'time18_focus{patrol_id}', '')
#
#         patrol.save()
#         return redirect('check:patrol_s_class')
#     return redirect('check:patrol_s_class')