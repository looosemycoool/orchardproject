from django.shortcuts import render

def attendance(request):
    return render(request, 'check/check_main.html')