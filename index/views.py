from django.shortcuts import render


def index(request):
    return render(request, 'index/jts_index.html')
