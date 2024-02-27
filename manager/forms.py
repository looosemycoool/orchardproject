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
        for field_name in ['mon_korean_lecture_study_hour', 'mon_korean_lecture_study_min', 'mon_korean_self_study_hour', 'mon_korean_self_study_min',
                           'mon_math_lecture_study_hour', 'mon_math_lecture_study_min', 'mon_math_self_study_hour', 'mon_math_self_study_min',
                           'mon_english_lecture_study_hour', 'mon_english_lecture_study_min', 'mon_english_self_study_hour', 'mon_english_self_study_min',
                           'mon_research_lecture_study_hour', 'mon_research_lecture_study_min', 'mon_research_self_study_hour']:
            self.fields[field_name].required = False
        self.fields['week_name'].required = True
        self.fields['start_date'].required = True
        self.fields['end_date'].required = True

    def clean(self):
        cleaned_data = super().clean()
        # 필드별로 None 체크 후 0으로 대체
        for field_name in ['mon_korean_lecture_study_hour', 'mon_korean_lecture_study_min', 'mon_korean_self_study_hour', 'mon_korean_self_study_min',
                           'mon_math_lecture_study_hour', 'mon_math_lecture_study_min', 'mon_math_self_study_hour', 'mon_math_self_study_min',
                           'mon_english_lecture_study_hour', 'mon_english_lecture_study_min', 'mon_english_self_study_hour', 'mon_english_self_study_min',
                           'mon_research_lecture_study_hour', 'mon_research_lecture_study_min', 'mon_research_self_study_hour']:
            if cleaned_data.get(field_name) is None:
                cleaned_data[field_name] = 0
        return cleaned_data


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