
class Cart():
    
    
    def __init__(self, request):
        
        self.session = request.session
        
        # Returning user - obtain their existing data/session
        cart = self.session.get('session_key')
        
        
        # New user - generate a new session
        
        if 'session_key' not in request.session:
            
            cart = self.session['session_key'] = {}
            
            
        self.cart = cart
        
    
    