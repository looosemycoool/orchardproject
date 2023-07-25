from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Reserve

from ..forms import CommentForm

@login_required(login_url="common:login")
def comment_create(request, reserve_id):
    reserve = Reserve.objects.get(id=reserve_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reserve.comment = form.cleaned_data['comment']
            reserve.save()
            teacher_id = reserve.teacher_id.id
            return redirect('reserve:detail', teacher_id=teacher_id)
    else:
        form = CommentForm(instance=reserve)
    return render(request, 'reserve/comment_form.html', {'form': form})


@login_required(login_url="common:login")
def comment_modify(request, reserve_id):
    reserve = get_object_or_404(Reserve, id=reserve_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=reserve)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.reserve = reserve
            comment.save()
            teacher_id = reserve.teacher_id.id
            return redirect('reserve:detail', teacher_id=teacher_id)
    else:
        form = CommentForm(instance=reserve)
    return render(request, 'reserve/comment_form.html', {'form': form})