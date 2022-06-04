from django.shortcuts import render
from django.http import HttpResponse




def information(request):
    return render(request, 'web_page.html')