from django.http import HttpResponse
from django.shortcuts import render

def index (request):

    return render(request, 'index.html')


   # return  HttpResponse("Home")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext= analyzed
       # return render(request, 'analyze.html', params)
    if(fullcaps == "on"):

        analyzed =  'analyzed'
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        for char in djtext:
            analyzed = ""
            for char in djtext:
                if char !="\n" and char!="\r":
                    analyzed = analyzed + char.upper()
            params = {'purpose': 'New lineremover', 'analyzed_text': analyzed}
            djtext = analyzed
           # return render(request, 'analyze.html', params)
    if (spaceremover == "on"):
        for char in djtext:
            analyzed = ""
            for char in djtext:
                if char != " ":
                    analyzed = analyzed + char
            params = {'purpose': 'space remover', 'analyzed_text': analyzed}
            djtext = analyzed
            #return render(request, 'analyze.html', params)
    if (extraspaceremover=="on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not(djtext[index] ==" " and djtext[index+1]==" "):
                    analyzed = analyzed + char
            params = {'purpose': 'extraspace remover', 'analyzed_text': analyzed}
    if(removepunc!="on" and fullcaps!= "on" and  newlineremover!="on" and spaceremover!="on" and extraspaceremover!="on" ):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)







