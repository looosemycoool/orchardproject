from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render, get_object_or_404, redirect
from ..models import Reserve, Teacher, Notice

from datetime import date
import datetime
@login_required(login_url='common:login')
def reserve(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    today = datetime.datetime.today().date()
    existing_reservation = Reserve.objects.filter(date=today, teacher_id=reserve.teacher_id,
                                                  student_name=request.user).exists()
    if not existing_reservation:
        reserve.student_name = request.user
        reserve.save()
        return render(request, 'reserve/reserve_complete.html', {'reserve': reserve})
    else:
        messages.warning(request, '이미 예약하였습니다.')
        return redirect('reserve:detail', teacher_id=reserve.teacher_id.id)


@login_required(login_url='common:login')
def reserve_delete(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    reserve.student_name = None
    reserve.save()
    return render(request, 'reserve/reserve_delete.html', {'reserve': reserve})
