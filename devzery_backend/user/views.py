# user/views.py

from django.http import JsonResponse
from django.contrib.sessions.models import Session
import json
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
            raise ValueError('Session deleted successfully')

        # Create a new session
        request.session.create()

        return JsonResponse({'status': 'success'})

    except Exception as e:
        # Handle exceptions and return an error response
        return JsonResponse({'status': 'error', 'message': str(e)})
