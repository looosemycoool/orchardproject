from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ..models import Student_Study_Data, Average_Study_Data
from check.models import StudentRegister
from ..forms import Student_Study_DataForm
from django.conf import settings
from collections import defaultdict

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def index(request):
    students = StudentRegister.objects.filter(is_dropped=False)
    context = {'students': students}
    return render(request, 'manager/word/word_main.html', context)