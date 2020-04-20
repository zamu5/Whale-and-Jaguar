from aylienapiclient import textapi
from django.shortcuts import render
from django.core.serializers import serialize


# Create your views here.
def index(request):
    endpoints = ['Sentiment', 'Classify', 'Entities', 'Concepts', 'Summarize']
    url = 'https://techcrunch.com/2019/12/22/who-will-the-winners-be-in-the-future-of-fintech/'
    data = {}
    client = textapi.Client('c0fcb430', '749f0eb9482c31ea51fb1b92a028231a')
    for endpoint in endpoints:
        command = 'client.' + endpoint + "({'url': url})"
        data[endpoint] = (eval(command))
    context = {'data': data}
    return render(request, 'home.html', context=context)
