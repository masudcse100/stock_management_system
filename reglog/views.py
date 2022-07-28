from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from . forms import SignUpForm,LoginForm
from django.contrib import messages
# Create your views here.

def signupView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Congratulations! You havbe become an Author!')
                form.save()
                return HttpResponseRedirect(reverse('account/login'))
        else:
            form = SignUpForm()
        return render(request, 'reglog/signup.html', {'form': form})
    else:
        return HttpResponseRedirect(reverse('index'))


def loginView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully!')
                    return HttpResponseRedirect(reverse('index'))
        else:
            form = LoginForm()
        return render(request, 'reglog/login.html',{'form': form})
    else:
        return HttpResponseRedirect(reverse('index'))


@login_required
def logoutView(request):
    logout(request)
    messages.success(request, 'Logout Successfully!')
    return HttpResponseRedirect(reverse('reglog:login'))

