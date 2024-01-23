from django.shortcuts import render, redirect
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
            profiles = AuthorizationUser.objects.values('name', 'age', 'profession', 'phone_number','location','unique_id','username',
                                                            'email_id')
            return JsonResponse({'status': 'success', 'profiles': list(profiles)})
        else:
            return JsonResponse({'status': 'error', 'message': 'Access denied'})
    except (Session.DoesNotExist, json.JSONDecodeError):
        return JsonResponse({'status': 'error', 'message': 'Invalid session token'})

@csrf_exempt
def logout_view(request):
    try:
        # Get the session token from the request data
        data = json.loads(request.body.decode('utf-8'))
        session_token = data.get('session_token')

        # Check if the session token is provided
        if not session_token:
            raise ValueError('Session token is missing in the request.')

        # Delete the session from the database
        deleted_count, _ = Session.objects.filter(session_key=session_token).delete()

        # Check if the session was deleted successfully
        if deleted_count == 0:
            raise ValueError('Session deleted successfully.')

        # Create a new session
        request.session.create()

        return JsonResponse({'status': 'success'})

    except Exception as e:
        # Handle exceptions and return an error response
        return JsonResponse({'status': 'error', 'message': str(e)})
