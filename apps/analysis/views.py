from aylienapiclient.errors import HttpError
from django.http import HttpResponse
from aylienapiclient import textapi
from django.shortcuts import render
from .forms import URL
import json


def home(request):
    if request.method == 'POST':
        form = URL(request.POST)
        if form.is_valid():
            endpoints = ['Sentiment', 'Classify', 'Entities', 'Concepts', 'Summarize']
            url = form.cleaned_data['url']
            data = {}
            client = textapi.Client('c0fcb430', '749f0eb9482c31ea51fb1b92a028231a')
            try:
                for endpoint in endpoints:
                    command = 'client.' + endpoint + "({'url': url})"
                    data[endpoint] = (eval(command))
                context = {'data': data}
                dump = json.dumps(context)
                if form.cleaned_data['type'][0] == 'json':
                    return HttpResponse(dump, content_type='application/json')
                elif form.cleaned_data['type'][0] == 'table':
                    context['form'] = URL()
                    return render(request, 'detail.html', context=context)
                else:
                    return HttpResponse(dump, content_type='text/x-json')
            except HttpError:
                return render(request, 'error.html', {'form': URL()})
    else:
        form = URL()
    return render(request, 'home.html', {'form': form})


