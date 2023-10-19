from django.shortcuts import render
from .models import Product, Contact
# from django.http import HttpResponse

# Create your views here.

def index(request):
    products = Product.objects.all()
    params = {'products': products}
    return render(request, "index.html", params)

def contact(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def search(request):
    return render(request, "search.html")

def productdetail(request, id):
    productdet = Product.objects.filter(id=id)
    return render(request, "productdetail.html", {'product': productdet[0]})

def checkout(request):
    return render(request, "checkout.html")