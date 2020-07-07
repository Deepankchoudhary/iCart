from math import ceil

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact


def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nslides = n // 4 + ceil((n / 4) - (n // 4))

    # params = {'no_of_slides':nslides,'range':range(1,nslides),'product': products}
    #  allprods=[[products, range(1,nslides),nslides],
    #            [products,range(1, nslides),nslides]]

    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])

    params = {'allprods': allprods}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/About.html")


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        mobile=request.POST.get('mobile','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,mobile=mobile,desc=desc)
        contact.save()

    return render(request, "shop/Contactus.html")


def track(request):
    return render(request, "shop/Tracking.html")


def search(request):
    return render(request, "shop/Search.html")


def product(request, myid):
    # fetch the product by its id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodview.html",{'product':product[0]})


def checkout(request):
    return render(request, "shop/Checkout.html")
