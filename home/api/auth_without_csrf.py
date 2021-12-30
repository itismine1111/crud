from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    
    # Overriding the function that was performing the csrf check 
    def enforce_csrf(self, request):
        return
