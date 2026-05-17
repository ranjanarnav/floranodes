from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import ContactMessageForm

def dashboard(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('dashboard')
        messages.error(request, "There was an error. Please check the form.")
    else:
        form = ContactMessageForm()

    return render(request, 'index.html', {'form': form})


def mc(request):
    return render(request, 'minecraft.html')


def vps(request):
    return render(request, 'vps.html')


def dc(request):
    return render(request, 'discord.html')


def tos(request):
    return render(request, 'tos.html')


def about(request):
    return render(request, 'about.html')


def itl(request):
    return render(request, 'intel-xeon.html')


def amd(request):
    return render(request, 'minecraft.html')


def ryz(request):
    return render(request, 'ryzen.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        messages.error(request, "There was an error. Please try again.")
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})

def rp(request):
    return render(request, 'refund_policy.html')


def pp(request):
    return render(request, 'privacy_policy.html')


def up(request):
    return render(request, 'usage_policy.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)
