from django.shortcuts import render, redirect
from reserve.models import Teacher
from ..forms import TeacherForm
from django.shortcuts import get_object_or_404
def teacher(request):
    teacher_list = Teacher.objects.all().order_by('id')
    context = {'teacher_list': teacher_list}
    return render(request, 'manager/teacher/teacher_check.html', context)


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)  # Create a Teacher instance but don't save it yet
            teacher.name = form.cleaned_data['name']
            teacher.subject = form.cleaned_data['subject']
            teacher.duty_day = form.cleaned_data['duty_day']
            teacher.duty_time = form.cleaned_data['duty_time']
            teacher.retired = form.cleaned_data['retired']
            teacher.save()  # Save the Teacher instance
            return redirect('manager:teacher')
    else:
        form = TeacherForm()

    return render(request, 'manager/teacher/teacher_form.html', {'form': form})

def teacher_modify(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('manager:teacher')
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'manager/teacher/teacher_form.html', {'form': form})
