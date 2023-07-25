from django import forms
from .models import Reserve

class CommentForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['comment']

        labels = {
            'comment': '코멘트',
        }