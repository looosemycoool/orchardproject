from django import forms
from .models import StudentRegister, Attendance, PatrolCheck

class StudentRegisterForm(forms.ModelForm):
    CHOICES = (
        ('False', ' '),
        ('korean', '국어'),
        ('math', '수학'),
        ('english', '영어'),
        ('research', '탐구'),
        ('guitar', '기타'),
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
        fields = ['student', 'teacher', 'username', 'class_name', 'class_num', 'register_date', 'drop_date', 'is_dropped']
    def __init__(self, *args, **kwargs):
        super(StudentRegisterForm, self).__init__(*args, **kwargs)

        # 필수 항목이 아닌 필드에 대해 required 속성을 False로 설정
        self.fields['student'].required = False
        self.fields['teacher'].required = False
        self.fields['username'].required = False
        self.fields['drop_date'].required = False

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['late', 'early_leave', 'absent']
        widgets = {
            'late': forms.TimeInput(attrs={'type': 'time'}),
            'early_leave': forms.TimeInput(attrs={'type': 'time'}),
            'absent': forms.CheckboxInput(),
        }
    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].required = False

class PatrolCheckForm(forms.ModelForm):
    STUDY_CHOICES = (
        ('False', ' '),
        ('k_ss', '국어자습'),
        ('k_il', '국어인강'),
        ('m_ss', '수학자습'),
        ('m_il', '수학인강'),
        ('e_ss', '영어자습'),
        ('e_il', '영어인강'),
        ('r_ss', '탐구자습'),
        ('r_il', '탐구인강'),
        ('sleep', '수면'),
    )
    FOCUS_CHOICES = (
        ('three', 3),
        ('two', 2),
        ('one', 1)
    )

    # time1_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time1_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    # time2_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time2_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time3_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time3_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time4_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time4_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time5_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time5_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time6_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time6_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time7_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time7_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time8_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time8_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time9_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time9_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time10_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time10_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time11_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time11_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time12_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time12_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time13_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time13_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time14_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time14_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time15_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time15_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time16_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time16_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time17_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time17_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    # time18_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    # time18_focus = forms.ChoiceField(choices=FOCUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = PatrolCheck  # 모델 클래스를 지정해야 함
        fields = ['time1_study', 'time1_focus']
        # widgets = {
        #     'time1_study': forms.Select(attrs={'class': 'form-control'}),
        #     'time1_focus': forms.Select(attrs={'class': 'form-control'})
        # }

    def __init__(self, *args, **kwargs):
        super(PatrolCheckForm, self).__init__(*args, **kwargs)
        for i in range(1, 19):  # 1부터 18까지의 필드를 생성합니다.
            self.fields[f'time{i}_study'] = forms.ChoiceField(
                choices=self.STUDY_CHOICES,
                widget=forms.Select(attrs={'class': 'form-control'})
            )
            self.fields[f'time{i}_focus'] = forms.ChoiceField(
                choices=self.FOCUS_CHOICES,
                widget=forms.Select(attrs={'class': 'form-control'})
            )