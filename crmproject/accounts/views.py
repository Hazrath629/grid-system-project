from django.shortcuts import render
def home(request):
    return render(request,'accounts/dashboard.html')
def orders(request):
    return render(request,'accounts/orders.html')
def products(request):
    return render(request,'accounts/products.html')
