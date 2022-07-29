from django.shortcuts import render, HttpResponseRedirect
from . forms import SignUpForm,CatForm
from django.contrib import messages
from . models import Categorie
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse('smsApps:index'))

@login_required
def index(request):
	cat_count = Categorie.objects.all().count()
	return render(request, 'smsApps/dashboard.html',{'cat_count':cat_count})

@login_required
def categoreyView(request):
	allcatn = Categorie.objects.all()
	return render(request, 'smsApps/categories.html',{'allcats':allcatn})

def addCategorey(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CatForm(request.POST)
            if form.is_valid():
                cat_name = form.cleaned_data['cat_name']
                cat_brand = form.cleaned_data['cat_brand']
                active = form.cleaned_data['active']
				# active = form
                post = Categorie(cat_name=cat_name, cat_brand=cat_brand, active=active)
                post.save()
                messages.success(request,'Add post successfull!')
                form = CatForm()
				# return HttpResponseRedirect(reverse('index'))
        else:
            form = CatForm()
        return render(request, 'smsApps/categoriesadd.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

