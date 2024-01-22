# authorisation/views.py
from django.shortcuts import render
from django.db import models
from .forms import SignupForm
from django.contrib.auth.hashers import make_password, check_password
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from .models import AuthorizationUser
from .forms import LoginForm
from django.core.exceptions import ObjectDoesNotExist

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
                return JsonResponse({'status': 'error', 'errors': form.errors})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'})
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
                        request.session['is_admin'] = user.is_admin
                        request.session.save()

                        # Return the session token in the response
                        return JsonResponse({'status': 'success', 'session_token': request.session.session_key})
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Invalid password'})
                except AuthorizationUser.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': 'User does not exist'})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'})
    else:
        form = LoginForm()

    return render(request, 'authorisation/login.html', {'form': form})
