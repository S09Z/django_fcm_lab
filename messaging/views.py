from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import MessageForm
from firebase_admin import messaging

def index(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            body = form.cleaned_data["body"]
            image = form.cleaned_data["image"]
            message = messaging.Message(
                notification=messaging.Notification(
                    title=subject,
                    body=body,
                    image=image
                ),
                topic="test"
            )
            response = messaging.send(message)
            return JsonResponse({"success": True, "response": response})
    else:
        form = MessageForm()
    return render(request, "messaging/index.html", {"form": form})

def subscribe(request):
    # Implement subscribe logic here
    return JsonResponse({"success": True, "message": "Subscribed to topic."})

def unsubscribe(request):
    # Implement unsubscribe logic here
    return JsonResponse({"success": True, "message": "Unsubscribed from topic."})
