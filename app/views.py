from django.shortcuts import render, redirect, HttpResponse
from.models import Product
from Dmart.urls import *
# Create your views here.

def all_products(request):
    product = Product.objects.all()
    return render(request, 'products.html', {"products":product})


def add_product(request):
    if request.method == "GET":
        return render(request, 'add_product.html')
    elif request.method == "POST":
        data = request.POST
        if not data.get("id"):
            Product.objects.create(name = data.get("name"),
                price = data.get("price"),
                packaging_date = data.get("packaging_date")),
        else:
            product = Product.objects.get(id = data.get("id"))
            product.name = data.get("name")
            product.price = data.get("price")
            product.packaging_date = data.get("packaging_date")
            product.save()
        return redirect("all_products")
    

def update_product(request,id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        return render(request,'add_product.html',{"products":product})
    

def expire_product(request,id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        product.expire_product = True
        product.save()
        return redirect("all_products")
    

def show_expire_product(request):
    product = Product.objects.filter(expire_product=True)
    return render(request, 'expire_product.html', {"products":product})


def restore_product(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        product.expire_product=False
        product.save()
        return redirect("show_expire_product")
    

def premanantly_expire_product(request, id):
    try:       
        product = Product.objects.get(id = id)
    except Product.DoesNotExist as msg:
        return HttpResponse(msg)
    else:
        product.delete()
        return redirect("all_products")
    

print("Software Engineer")
