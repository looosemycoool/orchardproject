from django import forms
from .models import Consulting


class ConsultingForm(forms.ModelForm):
    CHOICES = (
        ('new_counseling', '신규상담'),
        #('question', '질문'),
        ('mentoring', '멘토링'),
        # ('other', '기타'),
    )
    consulting_type = forms.ChoiceField(choices=CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-select'}), label='상담유형')
    other_consulting_type = forms.CharField(required=False, label='기타 상담 유형')

    class Meta:
        model = Consulting
        fields = ['date', 'teacher_id', 'student_name', 'consulting_type', 'consulting_subject',
                  'consulting_content']

        labels = {
            'date': '날짜',
            'teacher_id': '선생님',
            'student_name': '학생 이름',
            'consulting_type': '상담 유형',
            'consulting_subject': '상담 제목',
            'consulting_content': '상담 내용',
        }
