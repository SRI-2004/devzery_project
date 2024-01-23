# user/views.py

from django.contrib.sessions.models import Session
from django.http import JsonResponse
from authorisation.models import AuthorizationUser
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_user_details(request):
    try:
        # Assuming the session token is included in the JSON body
        data = json.loads(request.body.decode('utf-8'))
        session_token = data.get('session_token')

        print(f"Received session token: {session_token}")

        # Validate the session token
        session = Session.objects.get(session_key=session_token)
        user_id = session.get_decoded().get('_auth_user_id', None)

        print(f"User ID from session: {user_id}")

        if user_id is not None:
            # Use the user ID to filter the user details
            user_details = AuthorizationUser.objects.values('name', 'age', 'profession', 'phone_number','location','unique_id','username',
                                                            'email_id').get(unique_id=user_id)

            if user_details is not None:
                return JsonResponse({'status': 'success', 'user_details': user_details})
            else:
                return JsonResponse({'status': 'error', 'message': 'User does not exist'})
        else:
            return JsonResponse({'status': 'error', 'message': 'User ID not found in session'})
    except (Session.DoesNotExist, json.JSONDecodeError):
        return JsonResponse({'status': 'error', 'message': 'Invalid session token'})
    except AuthorizationUser.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User does not exist'})

def logout_view(request):
    # Get the current session
    session_key = request.session.session_key

    # Delete the session from the database
    Session.objects.filter(session_key=session_key).delete()

    # Create a new session
    request.session.create()