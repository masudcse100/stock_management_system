from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponseRedirect(reverse('smsApps:index'))

def logout_view(request):
    return HttpResponseRedirect(reverse('reglog:login'))

# def home(request):
#     return HttpResponseRedirect(reverse('smsApps:index'))