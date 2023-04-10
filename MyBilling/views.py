from django.shortcuts import render

# Create your views here.

def mybilling(request):
    return render(request, 'MyBilling.html')