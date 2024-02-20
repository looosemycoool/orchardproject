from django import forms
from reserve.models import Teacher
from .models import Student_Study_Data, WordTest, ConsultingReport, WeekPlan


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

class WeekPlanForm(forms.ModelForm):
    class Meta:
        model = WeekPlan
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(WeekPlanForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].required = False
        self.fields['week_name'].required = True
        self.fields['start_date'].required = True
        self.fields['end_date'].required = True

class WordTestForm(forms.ModelForm):
    class Meta:
        model = WordTest
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(WordTestForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].required = False
        self.fields['month'].required = True

class ConsultingReportForm(forms.ModelForm):
    class Meta:
        model = ConsultingReport
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ConsultingReportForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].required = False
        self.fields['month'].required = True