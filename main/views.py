from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainn(request):
    '''
    show HelloWord in main page
    '''
    context = {'like':'Django 棒棒'}
    return render(request, 'main/main.html', context)
    #return HttpResponse('HelloWord')

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')
