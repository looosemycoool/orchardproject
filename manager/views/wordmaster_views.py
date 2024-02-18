from django.shortcuts import render, redirect, get_object_or_404
from ..models import WordTest
from check.models import StudentRegister
from ..forms import WordTestForm

def index(request):


    context = {}

    return render(request, 'manager/word/word_main.html', context)