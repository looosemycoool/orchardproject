from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from reserve.models import Teacher

from ..models import Consulting
from ..forms import ConsultingForm

from django.core.paginator import Paginator

@user_passes_test(lambda u: u.is_staff, login_url='common:login')
def consulting_page(request):
    consulting = Consulting.objects.order_by('-id')
    teacher = Teacher.objects.order_by('id')

    page = request.GET.get('page', '1')
    paginator = Paginator(consulting, 15)
    page_obj = paginator.get_page(page)

    context = {'teacher': teacher, 'consulting': page_obj}
    return render(request, 'teacher/consulting/consulting_main.html', context)

@login_required(login_url='common:login')
def consulting_detail(request, consulting_id):
	consulting = Consulting.objects.get(id=consulting_id)
	context = {'consulting': consulting}
	return render(request, 'teacher/consulting/consulting_detail.html', context)


@login_required(login_url='common:login')
def consulting_create(request):
    if request.method == 'POST':
        form = ConsultingForm(request.POST)
        if form.is_valid():
            consulting = form.save(commit=False)
            consulting.teacher_name = request.user
            consulting_type = form.cleaned_data.get('consulting_type')
            if consulting_type == 'other':
                other_consulting_type = form.cleaned_data.get('other_consulting_type')
                consulting.consulting_type = other_consulting_type
            else:
                consulting.consulting_type = consulting_type
            consulting.save()
            return redirect('teacher:index')
    else:
        form = ConsultingForm()
    context = {'form': form}
    return render(request, 'teacher/consulting/consulting_form.html', context)