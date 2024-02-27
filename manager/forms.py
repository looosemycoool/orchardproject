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
                           'mon_research_lecture_study_hour', 'mon_research_lecture_study_min', 'mon_research_self_study_hour',
                           'tue_korean_lecture_study_hour', 'tue_korean_lecture_study_min', 'tue_korean_self_study_hour', 'tue_korean_self_study_min',
                           'tue_math_lecture_study_hour', 'tue_math_lecture_study_min', 'tue_math_self_study_hour', 'tue_math_self_study_min',
                           'tue_english_lecture_study_hour', 'tue_english_lecture_study_min', 'tue_english_self_study_hour', 'tue_english_self_study_min',
                           'tue_research_lecture_study_hour', 'tue_research_lecture_study_min', 'tue_research_self_study_hour',
                           'wed_korean_lecture_study_hour', 'wed_korean_lecture_study_min', 'wed_korean_self_study_hour', 'wed_korean_self_study_min',
                           'wed_math_lecture_study_hour', 'wed_math_lecture_study_min', 'wed_math_self_study_hour', 'wed_math_self_study_min',
                           'wed_english_lecture_study_hour', 'wed_english_lecture_study_min', 'wed_english_self_study_hour', 'wed_english_self_study_min',
                           'wed_research_lecture_study_hour', 'wed_research_lecture_study_min', 'wed_research_self_study_hour',
                           'thu_korean_lecture_study_hour', 'thu_korean_lecture_study_min', 'thu_korean_self_study_hour', 'thu_korean_self_study_min',
                           'thu_math_lecture_study_hour', 'thu_math_lecture_study_min', 'thu_math_self_study_hour', 'thu_math_self_study_min',
                           'thu_english_lecture_study_hour', 'thu_english_lecture_study_min', 'thu_english_self_study_hour', 'thu_english_self_study_min',
                           'thu_research_lecture_study_hour', 'thu_research_lecture_study_min', 'thu_research_self_study_hour',
                           'fri_korean_lecture_study_hour', 'fri_korean_lecture_study_min', 'fri_korean_self_study_hour', 'fri_korean_self_study_min',
                           'fri_math_lecture_study_hour', 'fri_math_lecture_study_min', 'fri_math_self_study_hour', 'fri_math_self_study_min',
                           'fri_english_lecture_study_hour', 'fri_english_lecture_study_min', 'fri_english_self_study_hour', 'fri_english_self_study_min',
                           'fri_research_lecture_study_hour', 'fri_research_lecture_study_min', 'fri_research_self_study_hour',
                           'sat_korean_lecture_study_hour', 'sat_korean_lecture_study_min', 'sat_korean_self_study_hour', 'sat_korean_self_study_min',
                           'sat_math_lecture_study_hour', 'sat_math_lecture_study_min', 'sat_math_self_study_hour', 'sat_math_self_study_min',
                           'sat_english_lecture_study_hour', 'sat_english_lecture_study_min', 'sat_english_self_study_hour', 'sat_english_self_study_min',
                           'sat_research_lecture_study_hour', 'sat_research_lecture_study_min', 'sat_research_self_study_hour',
                           'sun_korean_lecture_study_hour', 'sun_korean_lecture_study_min', 'sun_korean_self_study_hour', 'sun_korean_self_study_min',
                           'sun_math_lecture_study_hour', 'sun_math_lecture_study_min', 'sun_math_self_study_hour', 'sun_math_self_study_min',
                           'sun_english_lecture_study_hour', 'sun_english_lecture_study_min', 'sun_english_self_study_hour', 'sun_english_self_study_min',
                           'sun_research_lecture_study_hour', 'sun_research_lecture_study_min', 'sun_research_self_study_hour']:
            self.fields[field_name].required = False
        self.fields['week_name'].required = True
        self.fields['start_date'].required = True
        self.fields['end_date'].required = True

    def clean(self):
        cleaned_data = super().clean()
        # 각 필드별로 None 체크 후 0으로 대체
        for field_name in ['mon_korean_lecture_study_hour', 'mon_korean_lecture_study_min', 'mon_korean_self_study_hour', 'mon_korean_self_study_min',
                           'mon_math_lecture_study_hour', 'mon_math_lecture_study_min', 'mon_math_self_study_hour', 'mon_math_self_study_min',
                           'mon_english_lecture_study_hour', 'mon_english_lecture_study_min', 'mon_english_self_study_hour', 'mon_english_self_study_min',
                           'mon_research_lecture_study_hour', 'mon_research_lecture_study_min', 'mon_research_self_study_hour',
                           'tue_korean_lecture_study_hour', 'tue_korean_lecture_study_min', 'tue_korean_self_study_hour', 'tue_korean_self_study_min',
                           'tue_math_lecture_study_hour', 'tue_math_lecture_study_min', 'tue_math_self_study_hour', 'tue_math_self_study_min',
                           'tue_english_lecture_study_hour', 'tue_english_lecture_study_min', 'tue_english_self_study_hour', 'tue_english_self_study_min',
                           'tue_research_lecture_study_hour', 'tue_research_lecture_study_min', 'tue_research_self_study_hour',
                           'wed_korean_lecture_study_hour', 'wed_korean_lecture_study_min', 'wed_korean_self_study_hour', 'wed_korean_self_study_min',
                           'wed_math_lecture_study_hour', 'wed_math_lecture_study_min', 'wed_math_self_study_hour', 'wed_math_self_study_min',
                           'wed_english_lecture_study_hour', 'wed_english_lecture_study_min', 'wed_english_self_study_hour', 'wed_english_self_study_min',
                           'wed_research_lecture_study_hour', 'wed_research_lecture_study_min', 'wed_research_self_study_hour',
                           'thu_korean_lecture_study_hour', 'thu_korean_lecture_study_min', 'thu_korean_self_study_hour', 'thu_korean_self_study_min',
                           'thu_math_lecture_study_hour', 'thu_math_lecture_study_min', 'thu_math_self_study_hour', 'thu_math_self_study_min',
                           'thu_english_lecture_study_hour', 'thu_english_lecture_study_min', 'thu_english_self_study_hour', 'thu_english_self_study_min',
                           'thu_research_lecture_study_hour', 'thu_research_lecture_study_min', 'thu_research_self_study_hour',
                           'fri_korean_lecture_study_hour', 'fri_korean_lecture_study_min', 'fri_korean_self_study_hour', 'fri_korean_self_study_min',
                           'fri_math_lecture_study_hour', 'fri_math_lecture_study_min', 'fri_math_self_study_hour', 'fri_math_self_study_min',
                           'fri_english_lecture_study_hour', 'fri_english_lecture_study_min', 'fri_english_self_study_hour', 'fri_english_self_study_min',
                           'fri_research_lecture_study_hour', 'fri_research_lecture_study_min', 'fri_research_self_study_hour',
                           'sat_korean_lecture_study_hour', 'sat_korean_lecture_study_min', 'sat_korean_self_study_hour', 'sat_korean_self_study_min',
                           'sat_math_lecture_study_hour', 'sat_math_lecture_study_min', 'sat_math_self_study_hour', 'sat_math_self_study_min',
                           'sat_english_lecture_study_hour', 'sat_english_lecture_study_min', 'sat_english_self_study_hour', 'sat_english_self_study_min',
                           'sat_research_lecture_study_hour', 'sat_research_lecture_study_min', 'sat_research_self_study_hour',
                           'sun_korean_lecture_study_hour', 'sun_korean_lecture_study_min', 'sun_korean_self_study_hour', 'sun_korean_self_study_min',
                           'sun_math_lecture_study_hour', 'sun_math_lecture_study_min', 'sun_math_self_study_hour', 'sun_math_self_study_min',
                           'sun_english_lecture_study_hour', 'sun_english_lecture_study_min', 'sun_english_self_study_hour', 'sun_english_self_study_min',
                           'sun_research_lecture_study_hour', 'sun_research_lecture_study_min', 'sun_research_self_study_hour']:
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