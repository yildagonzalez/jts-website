from django.shortcuts import render

def jts_contact(request):
    return render(request, 'contact/contact.html')