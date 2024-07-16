from django.http import JsonResponse
from django.shortcuts import render
from .forms import MessageForm

def index(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            body = form.cleaned_data["body"]
            image = form.cleaned_data["image"]
            # Handle sending the message
    else:
        form = MessageForm()
    return render(request, "messaging/index.html", {"form": form})

def subscribe(request):
    return JsonResponse({"success": True, "message": "Subscribed to topic."})

def unsubscribe(request):
    return JsonResponse({"success": True, "message": "Unsubscribed from topic."})
