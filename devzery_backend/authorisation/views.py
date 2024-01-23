# authorisation/views.py

from .forms import SignupForm
from django.contrib.auth.hashers import make_password
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.urls import reverse

from django.http import JsonResponse
from .models import AuthorizationUser
from .forms import LoginForm
from django.contrib.auth.views import PasswordResetConfirmView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = SignupForm(data)

            if form.is_valid():
                # Hash the password before saving to the database
                form.cleaned_data['password'] = make_password(form.cleaned_data['password'])
                print(form.cleaned_data)
                form.save(commit=True)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors},status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'},status=400)
    else:
        form = SignupForm()
    return render(request, 'authorisation/signup.html', {'form': form})
@csrf_exempt


def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = LoginForm(data)

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                try:
                    user = AuthorizationUser.objects.get(username=username)

                    if password == user.password:
                        # Generate a session token
                        request.session['_auth_user_id'] = user.unique_id

                        # Print session key and data for debugging
                        print(f"Session Key: {request.session.session_key}")
                        print(f"Session Data: {request.session._session}")

                        request.session['is_admin'] = user.is_admin
                        request.session['id'] = user.unique_id
                        request.session['username'] = user.username
                        request.session.save()

                        # Return the session token in the response
                        return JsonResponse({'status': 'success', 'session_token': request.session.session_key})
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Invalid password'},status=401)
                except AuthorizationUser.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': 'User does not exist'},status=400)
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'})
    else:
        form = LoginForm()

    return render(request, 'authorisation/login.html', {'form': form})

@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email_id=email)
            token = default_token_generator.make_token(user)
            reset_url = reverse('reset_password', kwargs={'email': email, 'token': token})

            reset_link = request.build_absolute_uri(reset_url)

            # Send an email with the reset link
            subject = 'Password Reset'
            message = f'Click the following link to reset your password: {reset_link}'
            send_mail(subject, message, 'from@example.com', [email])

            messages.success(request, 'A password reset link has been sent to your email.')
            return render(request, 'authorisation/forgot_password.html')
        except User.DoesNotExist:
            messages.error(request, 'No user found with the provided email address.')

    return render(request, 'authorisation/forgot_password.html')
@csrf_exempt

def reset_password(request, email, token):
    try:
        user = User.objects.get(email_id=email)
        if default_token_generator.check_token(user, token):
            return PasswordResetConfirmView.as_view(template_name='authorisation/reset_password.html',
                                                    success_url='/password_reset_complete/')(request, uidb64=user.id, token=token)
        else:
            messages.error(request, 'Invalid password reset link.')
            return render(request, 'authorisation/reset_password.html')
    except User.DoesNotExist:
        messages.error(request, 'Invalid password reset link.')
        return render(request, 'authorisation/reset_password.html')
@csrf_exempt
def verify_email(request, email, token):
    try:
        user = User.objects.get(email=email)
        # Check if the token is valid
        if default_token_generator.check_token(user, token):
            # Mark the user as verified
            user.is_active = True
            user.save()

            messages.success(request, 'Email verification successful. You can now log in.')
            return render(request, 'authorisation/verify_email.html')
        else:
            messages.error(request, 'Invalid verification link.')
            return render(request, 'authorisation/verify_email.html')
    except User.DoesNotExist:
        messages.error(request, 'Invalid verification link.')
        return render(request, 'authorisation/verify_email.html')
