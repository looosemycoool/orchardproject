from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import StudentRegister, Attendance

class StudentRegisterForm(forms.ModelForm):
    CHOICES = (
        ('False', ' '),
        ('korean', '국어'),
        ('math', '수학'),
        ('english', '영어'),
        ('research', '탐구'),
        ('guitar', '기타'),
        ('specify', '특이')
    )
    # 월요일
    mon8 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon9 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon10 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon11 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon12 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon13 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon14 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon15 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon16 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon17 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon18 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon19 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon20 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon21 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mon22 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # 화요일
    tue8 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue9 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue10 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue11 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue12 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue13 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue14 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue15 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue16 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue17 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue18 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue19 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue20 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue21 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    tue22 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # 수요일
    wed8 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed9 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed10 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed11 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed12 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed13 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed14 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed15 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed16 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed17 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed18 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed19 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed20 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed21 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    wed22 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # 목요일
    thu8 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu9 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu10 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu11 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu12 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu13 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu14 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu15 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu16 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu17 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu18 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu19 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu20 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu21 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    thu22 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # 금요일
    fri8 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri9 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri10 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri11 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri12 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri13 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri14 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri15 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri16 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri17 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri18 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri19 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri20 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri21 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    fri22 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # 토요일
    sat8 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat9 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat10 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat11 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat12 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat13 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat14 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat15 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat16 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat17 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat18 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat19 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat20 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat21 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sat22 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # 일요일
    sun8 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun9 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun10 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun11 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun12 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun13 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun14 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun15 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun16 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun17 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun18 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun19 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun20 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun21 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    sun22 = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = StudentRegister
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentRegisterForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].required = False
        self.fields['student'].required = True

    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get("student")

        # 현재 인스턴스의 ID 가져오기 (수정하는 경우에만 존재함)
        current_id = self.instance.id if self.instance else None

        # 'student' 필드에 대한 중복 확인 (현재 인스턴스 제외)
        if student and StudentRegister.objects.filter(student=student).exclude(id=current_id).exists():
            self.add_error('student', ValidationError(_("이미 등록된 학생입니다.")))

        return cleaned_data

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['morning_late', 'lunch_late', 'night_late', 'morning_check', 'lunch_check', 'night_check', 'early_leave', 'absent', 'memo']
        widgets = {
            'morning_late': forms.TimeInput(attrs={'type': 'time'}),
            'lunch_late': forms.TimeInput(attrs={'type': 'time'}),
            'night_late': forms.TimeInput(attrs={'type': 'time'}),
            'early_leave': forms.TimeInput(attrs={'type': 'time'}),
            'morning_check': forms.CheckboxInput(),
            'lunch_check': forms.CheckboxInput(),
            'night_check': forms.CheckboxInput(),
            #####
            'time8_check': forms.CheckboxInput(),
            'time9_check': forms.CheckboxInput(),
            'time10_check': forms.CheckboxInput(),
            'time11_check': forms.CheckboxInput(),
            'time12_check': forms.CheckboxInput(),
            'time13_check': forms.CheckboxInput(),
            'time14_check': forms.CheckboxInput(),
            'time15_check': forms.CheckboxInput(),
            'time16_check': forms.CheckboxInput(),
            'time17_check': forms.CheckboxInput(),
            'time18_check': forms.CheckboxInput(),
            'time19_check': forms.CheckboxInput(),
            'time20_check': forms.CheckboxInput(),
            'time21_check': forms.CheckboxInput(),
            'time22_check': forms.CheckboxInput(),
            'absent': forms.CheckboxInput(),
            'memo': forms.Textarea()
        }
    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].required = False
