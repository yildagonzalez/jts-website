from django.shortcuts import render

def jts_about(request):
    return render(request, 'about/about.html')