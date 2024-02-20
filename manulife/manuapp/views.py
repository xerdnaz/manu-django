from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def clients(request):
    return render(request, 'clients.html')

def addclient(request):
    return render(request, 'addclient.html')
