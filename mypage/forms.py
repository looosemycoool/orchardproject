from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from reserve.models import Teacher
from .models import Planner


class PlannerForm(forms.ModelForm):
    class Meta:
        model = Planner
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(PlannerForm, self).__init__(*args, **kwargs)
    #     for field_name in self.fields.keys():
    #         self.fields[field_name].required = False
    #     self.fields['date'].required = True