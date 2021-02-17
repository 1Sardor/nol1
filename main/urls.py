from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('shop', shop, name='shop'),
    path('wishlist', wishlist, name='wishlist'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('category', category, name='category'),
    path('add-savatcha', addtoBasket, name='add-savatcha'),
    path('delete-cart/', DeleteCart, name='delete-cart'),
    path('delete-wish/', DeleteWishlist, name='delete-wish'),
    path('Tanlangan', addWish, name='Tanlangan'),
    path('productqty', productqty, name='productqty'),    
    path('productdetail/<int:pk>', ProductDetail.as_view(), name='productdetail'),
]