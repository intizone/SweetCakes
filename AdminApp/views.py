from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404




def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')
def checkout(request):
    return render(request, 'checkout.html')
def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')
def myaccount(request):
    return render(request, 'myaccount.html')
def products(request):
    return render(request, 'products.html')
def register(request):
    return render(request, 'register.html')


def view_offers(request):
    try:
        offers = Offers.objects.all()
        response_content = ""
        for offer in offers:
            response_content += f"Offers: {offer.title}, {offer.details}, {offer.icon}\n"
        return HttpResponse(response_content)
    except Offers.DoesNotExist:
        return HttpResponse("No offers found")
    
def view_goods(request):
    try:
        goods = Goods.objects.all()
        response_content = ""
        for good in goods:
            response_content += f"Goods: {good.details}, {good.price}, {good.img}\n"
        return HttpResponse(response_content)
    except Goods.DoesNotExist:
        return HttpResponse("No goods found")

def update_offer(request):
    try:
        offer = Offers.objects.get(id=1)
        offer.title = 'Updated Title'
        offer.details = 'Updated Details'
        offer.icon = 'updated_image.jpg'
        offer.save()
        return HttpResponse("Offer updated successfully")
    except Offers.DoesNotExist:
        raise Http404("Offer does not exist")

def update_good(request):
    try:
        good = Goods.objects.get(id=1)
        good.details = 'Updated Details'
        good.price = 'Updated Price'
        good.img = 'updated_image.jpg'
        good.save()
        return HttpResponse("Good updated successfully")
    except Goods.DoesNotExist:
        raise Http404("Good does not exist")

def delete_offer(request):
    try:
        offer = Offers.objects.get(id=1)
        offer.delete()
        return HttpResponse("Offer deleted successfully")
    except Offers.DoesNotExist:
        raise Http404("Offer does not exist")

def delete_good(request):
    try:
        good = Goods.objects.get(id=1)
        good.delete()
        return HttpResponse("Good deleted successfully")
    except Goods.DoesNotExist:
        raise Http404("Good does not exist")

def create_offer(request):
    try:
        offer = Offers(title = 'New Title', details = 'New Details', icon = 'new_image.jpg')
        offer.save()
        return HttpResponse("Offer created successfully")
    except Offers.DoesNotExist:
        raise Http404("Offer does not exist")

def create_good(request):
    try:
        good = Goods(details = 'New Details', price = 'New Price', img = 'new_image.jpg')
        good.save()
        return HttpResponse("Good created successfully")
    except Goods.DoesNotExist:
        raise Http404("Good does not exist")

# def main(request):
#     return render(request, 'index.html')