#Nihal Created
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("<h1>hello</h1>")

def about(request):
    return HttpResponse("World")

def analyze(request):
    #Get text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    #analyzed = djtext
    punctuations = '''!@#$%^&*()_+-=[]{};':",./<>?'''
    analyzed = ""
    for char in djtext:
        if char not in punctuations:
            analyzed = analyzed + char

    params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    #Analyze text
    return render(request, 'analyze.html', params)

#def capfirst(request):
#    return HttpResponse("capitalize first")

#def newlineremove(request):
#    return HttpResponse("newlineremove")

#def spaceremove(request):
#    return HttpResponse("spaceremove")

#def charcount(request):
#    return HttpResponse("Charcount")