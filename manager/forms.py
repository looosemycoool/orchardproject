from django import forms
from reserve.models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'duty_day', 'duty_time', 'retired']

        labels = {
            'name': '이름',
            'subject': '과목',
            'duty_day': '요일',
            'duty_time': '시간',
            'retired': '퇴직'
        }