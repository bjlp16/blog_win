from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def article(request):
    '''
    Render the article page
    '''
    return render(request, 'article/article.html')
    #return HttpResponse('HelloWord')
