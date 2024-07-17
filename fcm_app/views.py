# fcm_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FCMTokenForm, FCMMessageForm
from .models import FCMToken
import requests
from django.conf import settings
from firebase_admin import messaging
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm

def home(request):
    return render(request, 'fcm_app/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'fcm_app/signup.html', {'form': form})

@login_required
def subscribe(request):
    if request.method == 'POST':
        form = FCMTokenForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            if not FCMToken.objects.filter(token=token, user=request.user).exists():
                fcm_token = form.save(commit=False)
                fcm_token.user = request.user
                fcm_token.save()
                messages.success(request, 'Successfully subscribed!')
            else:
                messages.info(request, 'You are already subscribed with this token.')
            return redirect('subscribe')
    else:
        form = FCMTokenForm()
    tokens = FCMToken.objects.filter(user=request.user)
    return render(request, 'fcm_app/subscribe.html', {'form': form, 'tokens': tokens})

@login_required
def send_message(request):
    tokens = FCMToken.objects.filter(user=request.user).values_list('token', flat=True)
    if request.method == 'POST':
        form = FCMMessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            response = send_fcm_message(tokens, title, body)
            if response:
                messages.success(request, 'Message sent successfully!')
            else:
                messages.error(request, 'Failed to send the message.')
            return redirect('send_message')
    else:
        form = FCMMessageForm()
    return render(request, 'fcm_app/send_message.html', {'form': form, 'tokens': tokens})

@login_required
def unsubscribe(request, token_id):
    token = get_object_or_404(FCMToken, id=token_id, user=request.user)
    token.delete()
    messages.success(request, 'Successfully unsubscribed!')
    return redirect('subscribe')

def send_fcm_message(tokens, title, body):
    message = messaging.MulticastMessage(
        tokens=list(tokens),
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
    )
    response = messaging.send_multicast(message)
    return response.success_count