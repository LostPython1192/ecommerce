
class Cart():
    
    
    def __init__(self, request):
        
        self.session = request.session
        
        # Returning user - obtain their existing data/session
        cart = self.session.get('session_key')
        
        
        # New user - generate a new session
        
        if 'session_key' not in request.session:
            
            cart = self.session['session_key'] = {}
            
            
        self.cart = cart
        
    
    
def add(self, product, product_qty):

    product_id = str(product.id)

    if product_id in self.cart: # If already in cart, only updating the qty

        self.cart[product_id]['qty'] = product_qty

    else: # Not in the current cart

        self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}

    self.session.modified = True