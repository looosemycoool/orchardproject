from django.shortcuts import render, redirect
from ..models import Reserve
from ..forms import ConsultForm

def consult_create(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    if request.method == 'POST':
        form = ConsultForm(request.POST)
        if form.is_valid():
            reserve.type = form.cleaned_data.get('type')
            reserve.subject = form.cleaned_data['subject']
            reserve.content = form.cleaned_data['content']
            reserve.title = form.cleaned_data['title']
            reserve.save()
            teacher_id = reserve.teacher_id.id
            return redirect('reserve:detail', teacher_id=teacher_id)
    else:
        form = ConsultForm()

    return render(request, 'reserve/consult_form.html', {'form': form, 'reserve': reserve})

def consult_modify(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    if request.method == 'POST':
        form = ConsultForm(request.POST, instance=reserve)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.save()
            teacher_id = reserve.teacher_id.id
            return redirect('reserve:detail', teacher_id=teacher_id)
    else:
        form = ConsultForm(instance=reserve)

    return render(request, 'reserve/consult_form.html', {'form': form, 'reserve': reserve})
