
"""
Now that you have a Cart class to manage the cart, you need to create the views 
to add, update, or remove items from it. You need to create the following views:
• A view to add or update items in the cart that can handle current and new 
quantities
• A view to remove items from the cart
• A view to display cart items and totals
"""
from django.shortcuts import render,redirect,get_object_or_404
from .cart import Cart
from apps.cart.forms import CartAddProductForm
from apps.dashboard.models import ProductModel
from django.views.decorators.http import require_POST

# Create your views here.

@require_POST
def cart_add(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(ProductModel,id=product_id)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.addproducts2cart(product,quantity=cd['quantity'],override_quantity=cd['override'])   
    return redirect('cart_detail')

@require_POST
def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(ProductModel,id=product_id)
    cart.removeproduct_from_cart(product=product)
    return redirect('cart_detail')


#display cart and its details

def cart_details(request):
    cart=Cart(request)
    return redirect(request,'cart/cart_detail.html',{'cart':cart})

