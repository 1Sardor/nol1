from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.

def PagenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')

    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list



def index(request):
    product = Product.objects.all().order_by('-id')[0:6]

    context = {
        'product':product,
    }
    return render(request, 'index.html', context)


def wishlist(request):
    user = request.user
    product = Tanlangan.objects.filter(User=user)
    context = {
        'product':product,
    }
    return render(request, 'wishlist.html', context)

def shop(request):
    product = Product.objects.all().order_by('-id')
    category = Category.objects.all()
    page = request.GET.get('page') 

    context = {
        'product': PagenatorPage(product, 3, request),
        'category':category,
        'page':page,
    }
    return render(request, 'shop.html', context)

def cart(request):
    user = request.user
    product = Savatcha.objects.filter(User=user)
    context = {
        'product':product,
    }
    return render(request, 'cart.html', context)

def checkout(request):
    return render(request, 'checkout.html')

def category(request):
    category = request.GET['c']
    product = Product.objects.filter(cat__name=category)
    category = Category.objects.all()
    context = {
        'product':product,
        'category':category,
    }
    return render(request, 'category.html', context)


def addtoBasket(request):
    m_id = request.GET.get("m_id")
    quan = request.GET.get("quan")
    user = request.user
    prod = Product.objects.get(id=m_id)
    savat = Savatcha.objects.create(User=user, product=prod, quantity=quan)
    savat.save()
    data = {}

    return JsonResponse(data)

def addWish(request):
    m_id = request.GET.get("m_id")
    user = request.user
    prod = Product.objects.get(id=m_id)
    tanlang = Tanlangan.objects.create(User=user, product=prod)
    tanlang.save()
    data = {}

    return JsonResponse(data)


def DeleteCart(request):
    if request.method == 'GET':
        c_id = request.GET.get('c_id')
        Savatcha.objects.get(id=c_id).delete()
    return redirect('cart')

def DeleteWishlist(request):
    if request.method == "GET":
        c_id = request.GET.get('c_id')
        Tanlangan.objects.get(id=c_id).delete()
    return redirect('wishlist')

    
def productqty(request):
    if request.method == "POST":
        soni = request.POST.get('qty')
        print(soni)

    redirect('cart')


class ProductDetail(DetailView):
    template_name = "productdetail.html"
    model = Product
    context_object_name = "product"
    product = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["product1"] = Product.objects.first()

        return context
