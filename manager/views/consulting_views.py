from django.shortcuts import render

def consulting(request):
    return render(request, 'manager/consulting/manager_consulting_main.html')

def consulting_detail(request):
    return render(request, 'manager/consulting/manager_consulting_detail.html')