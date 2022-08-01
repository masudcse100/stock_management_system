from django.shortcuts import render, HttpResponseRedirect
from requests import request
from . forms import SignUpForm,CatForm
from django.contrib import messages
from . models import Categorie
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return HttpResponseRedirect(reverse('smsApps:index'))

@login_required
def index(request):
	categories_count = Categorie.objects.all().count()
	# product_count = Categorie.objects.all().count()
	# cat_count = Categorie.objects.all().count()
	return render(request, 'smsApps/dashboard.html',{'cat_count':categories_count})

@login_required
def categoreyView(request):
    allcats = Categorie.objects.all().order_by('cat_name')
    pagntr = Paginator(allcats, 5)
    page_num = request.GET.get('cat_page')
    page_obj = pagntr.get_page(page_num)
    return render(request, 'smsApps/categories.html',{'page_cat_obj':page_obj})

def addCategorey(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CatForm(request.POST)
            if form.is_valid():
                cat_name = form.cleaned_data['cat_name']
                cat_brand = form.cleaned_data['cat_brand']
                status = form.cleaned_data['status']
				# active = form
                # post = Categorie(cat_name=cat_name, cat_brand=cat_brand, active=active)
                post = Categorie(cat_name=cat_name, cat_brand=cat_brand, status=status)
                post.save()
                messages.success(request,'Add post successfull!')
                form = CatForm()
				# return HttpResponseRedirect(reverse('index'))
        else:
            form = CatForm()
        return render(request, 'smsApps/categoriesadd.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

# def save_category(request):
#     return render(request, 'smsApps/modaltest.html')