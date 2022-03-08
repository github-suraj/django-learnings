from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def homepage(request):
    return render(request, 'home.html')

def counter(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = sorted(Counter(wordlist).items())
    _dict = dict(fulltext=fulltext, count=wordlist.__len__(), worddict=worddict)
    return render(request, 'count.html', _dict)

def about(request):
    return HttpResponse("<h1>This is word counter website</h1><a href='/'>Count</a>")
