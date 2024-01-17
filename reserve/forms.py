from django import forms
from .models import Reserve, Notice

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
        ('study_counseling', '학습상담'),
        ('mentoring', '멘토링'),
    )
    type = forms.ChoiceField(choices=CHOICES,
                             widget=forms.Select(attrs={'class': 'form-select'}), label='상담 유형')

    SUBJECT_CHOICES = (
        ('korean', '국어'),
        ('math', '수학'),
        ('english', '영어'),
        ('chemistry', '화학'),
        ('biology', '생명과학'),
        ('physics', '물리'),
        ('earth', '지구과학'),
        ('science', '통합과학'),
        ('social', '사회탐구'),
    )
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES,
                             widget=forms.Select(attrs={'class': 'form-select'}), label='과목')

    class Meta:
        model = Reserve
        fields = ['subject', 'type', 'title', 'content']

        labels = {
            'subject': '과목',
            'type': '상담 유형',
            'title': '제목',
            'content': '내용',
        }

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['notice_header', 'notice_body']

        labels = {
            'notice_header': '제목',
            'notice_body': '내용'
        }
