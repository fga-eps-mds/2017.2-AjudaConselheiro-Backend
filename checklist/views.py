from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Create your views here.
def checklist1(request):
    return render(request, 'checklists/checklist1.html')

def checklist2(request):
    return render(request, 'checklists/checklist2.html')

def checklist3(request):
    return render(request, 'checklists/checklist3.html')
