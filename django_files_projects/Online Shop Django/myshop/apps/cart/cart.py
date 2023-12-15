from decimal import Decimal
from django.conf import settings
from apps.dashboard.models import ProductModel


#Cart class  to manage shopping carts.

class Cart(object):
    """Initialize the Cart"""
    """First, you try to get the cart from the current session using self.session.
    get(settings.CART_SESSION_ID). If no cart is present in the session, you create 
    an empty cart by setting an empty dictionary in the session."""
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)

        if not cart: # save empty cart in session
            cart=self.session[settings.CART_SESSION_ID] ={}
        self.cart=cart

    def addproducts2cart(self, product, quantity=1, override_quantity=False):
        """Add product or update the quantity"""
        """. You convert the 
        product ID into a string because Django uses JSON to serialize session data, and 
        JSON only allows string key names."""

        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,'price':str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            self.savingproduct2cart()

    def savingproduct2cart(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def removeproduct_from_cart(self,product):
        product_id=str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.savingproduct2cart()

    def __iter__(self):
        """You will have to iterate through the items contained in the cart and access the related 
            Product instances."""
        
        product_ids = self.cart.keys()
 # get the product objects and add them to the cart
        products = ProductModel.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item 
        in self.cart.values())
    






