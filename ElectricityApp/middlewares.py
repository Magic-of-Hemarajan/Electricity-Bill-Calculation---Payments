from django.utils import timezone
import datetime
# from datetime import timedelta
from django.conf import settings
from django.contrib.sessions.models import Session

class SessionExpiryMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        # if hasattr(request,'user') and request.user.is_authenticated:
            session = request.session
            now = timezone.now()
            last_activity = session.get('last_activity')
            
            if last_activity and (now-last_activity).second > 120:
                # from django.contrib.auth import logout 
                # logout(request)
                request.session.flush()
            else:
                request.session['last_activity']=now
                response = self.get_response
                return response