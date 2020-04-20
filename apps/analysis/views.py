from aylienapiclient import textapi
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import URL


def home(request):
    if request.method == 'POST':
        form = URL(request.POST)
        if form.is_valid():
            endpoints = ['Sentiment', 'Classify', 'Entities', 'Concepts', 'Summarize']
            url = form.cleaned_data['url']
            data = {}
            client = textapi.Client('c0fcb430', '749f0eb9482c31ea51fb1b92a028231a')
            for endpoint in endpoints:
                command = 'client.' + endpoint + "({'url': url})"
                data[endpoint] = (eval(command))
            context = {'data': data}
            return render(request, 'detail.html', context=context)
    else:
        form = URL()
    return render(request, 'home.html', {'form': form})

