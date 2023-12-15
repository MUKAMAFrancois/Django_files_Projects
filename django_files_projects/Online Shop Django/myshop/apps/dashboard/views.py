from django.shortcuts import render, get_object_or_404
from apps.dashboard.models import  ProductModel
from django.views.generic import DetailView
from apps.cart.forms import CartAddProductForm


def listing_products(request):
    laptops=ProductModel.objects.filter(category='laptops')
    gadgets=ProductModel.objects.filter(category='gadgets')
    phones=ProductModel.objects.filter(category='phones')
    
    dictionary={
        'laptops':laptops,
        'gadgets':gadgets,
        'phones':phones
    }

    return render(request, 'dashboard/products/list_products.html',dictionary)

def explore_laptops(request):
    laptops=ProductModel.objects.filter(category='laptops')
    return render(request,'dashboard/products/explore_laptop.html',{'laptops':laptops})

def explore_phones(request):
    phones=ProductModel.objects.filter(category='phones')
    return render(request,'dashboard/products/explore_phone.html',{'phones':phones})


def explore_gadgets(request):
    gadgets=ProductModel.objects.filter(category='gadgets')
    return render(request,'dashboard/products/explore_gadgets.html',{'gadgets':gadgets})




def product_detail(request, id, slug):
    product = get_object_or_404(ProductModel, id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    
    mb={'product': product,
         'cart_product_form': cart_product_form}
    
    return render(request,'dashboard/products/details.html',mb)


#class Details(DetailView):
 #   model=ProductModel
  #  context_object_name='product'
   # template_name='dashboard/products/details.html'
   

