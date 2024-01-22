from django.shortcuts import render
# admin/views.py
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse
from authorisation.models import AuthorizationUser
import json

@csrf_exempt
def get_profiles(request):
    try:
        # Assuming the session token is included in the JSON body
        data = json.loads(request.body.decode('utf-8'))
        session_token = data.get('session_token')

        print(f"Received session token: {session_token}")

        # Validate the session token
        session = Session.objects.get(session_key=session_token)
        is_admin = session.get_decoded().get('is_admin')

        print(f"Session is_admin: {is_admin}")

        if is_admin:
            profiles = AuthorizationUser.objects.values('name', 'age', 'profession', 'phone_number', 'email_id')
            return JsonResponse({'status': 'success', 'profiles': list(profiles)})
        else:
            return JsonResponse({'status': 'error', 'message': 'Access denied'})
    except (Session.DoesNotExist, json.JSONDecodeError):
        return JsonResponse({'status': 'error', 'message': 'Invalid session token'})
