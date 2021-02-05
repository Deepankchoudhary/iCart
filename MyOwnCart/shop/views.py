from math import ceil

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
import json


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
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, mobile=mobile, desc=desc)
        contact.save()

    return render(request, "shop/Contactus.html")


# def track(request):
#     return render(request, "shop/Tracking.html")


def search(request):
    return render(request, "shop/Search.html")


def product(request, myid):
    # fetch the product by its id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodview.html", {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city,
                      state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')


def track(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = checkout.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception:
            return HttpResponse('{}')

    return render(request, 'shop/Tracking.html')


def practice(request):
    return render(request, 'shop/Practice.html');
