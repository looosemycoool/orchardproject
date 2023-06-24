from django import forms
from .models import Reserve


class CommentForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['comment_subject', 'comment_content']

        labels = {
            'comment_subject': '제목',
            'comment_content': '내용',
        }