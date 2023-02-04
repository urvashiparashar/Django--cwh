# I have created this file-Urvashi
#code for video 6
from django.http import HttpResponse
from django.shortcuts import render
#code for video 7
def index(request):
    
    return render(request,'index.html')
#navigation tab
# def ex1(request):
#     s='''<h2>Navigation Bar</h2>
#     <a href="https://www.youtube.com/">Django with harry</a><br>
#     <a href=https://www.facebook.com/">Facebook</a><br>
#     <a href=https://www.flipkart.com/">FlipKart</a><br>
#     <a href=https://www.hindustan.com/">News</a><br>
#     <a href=https://www.google.com/>Google</a><br>'''
#     return HttpResponse(s)
def analyze(request):
    #get text
    #ste check box values
    djtext=request.POST.get('text','default')
    print(djtext)
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    
    if removepunc=="on":
       punctuations='''!()-{}[];:'",.\/<>?#@$&*%_~'''
       analyzed = ""
       for char in djtext:
        if char not in punctuations:
            analyzed=analyzed+char
       params={'purpose':'remove punctuations','analyzed_text':analyzed}
       djtext=analyzed
       # return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    if(newlineremove=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
             analyzed = analyzed + char
            else:
                print("no")
        print("pre",analyzed)  
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
    if(removepunc!="on" and newlineremove!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Please select any operation and try again")

        
    return render(request, 'analyze.html', params)

# def capitalize(request):
#     return HttpResponse("Capitalize first")
# def newlineremove(request):
#     return HttpResponse("New line remove")
# def spaceremove(request):
#     return HttpResponse("Space remove<a href='/'>Back</a>")
# def charcount(request):
#     return HttpResponse("Char count")
