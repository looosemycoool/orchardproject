from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from reserve.models import Teacher
from .models import Student_Study_Data

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

class Student_Study_DataForm(forms.ModelForm):
    class Meta:
        model = Student_Study_Data
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Student_Study_DataForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].required = False
        self.fields['week_name'].required = True
        self.fields['start_date'].required = True
        self.fields['end_date'].required = True

    # def clean(self):
    #     cleaned_data = super().clean()
    #     week_name = cleaned_data.get("week_name")
    #
    #     # 현재 인스턴스의 ID 가져오기 (수정하는 경우에만 존재함)
    #     current_id = self.instance.id if self.instance else None
    #
    #     # 'student' 필드에 대한 중복 확인 (현재 인스턴스 제외)
    #     if week_name and Student_Study_Data.objects.filter(week_name=week_name).exclude(id=current_id).exists():
    #         self.add_error('week_name', ValidationError(_("이미 등록된 기간입니다.")))
    #
    #     return cleaned_data

