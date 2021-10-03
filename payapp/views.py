from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'payapp/main.html')

def pay(request):
    return render(request, 'payapp/pay.html')