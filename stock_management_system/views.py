from django.shortcuts import  render
from django.contrib.auth import authenticate

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'smsApps/dashboad.html')




# def home(request):
#     return HttpResponseRedirect(reverse('smsApps:index'))
