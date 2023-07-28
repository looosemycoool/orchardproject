from django import forms
from .models import Reserve

class CommentForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['comment']

        labels = {
            'comment': '코멘트',
        }

# forms.py
class ConsultForm(forms.ModelForm):
    CHOICES = (
        ('question', '질의응답'),
        ('new_counseling', '초기상담'),
        ('study_conseling', '학습상담'),
        ('mentoring', '멘토링'),
    )
    type = forms.ChoiceField(choices=CHOICES,
                             widget=forms.Select(attrs={'class': 'form-select'}), label='상담 유형')
    class Meta:
        model = Reserve
        fields = ['type', 'subject', 'content']

        labels = {
            'type': '상담 유형',
            'subject': '제목',
            'content': '내용',
        }
