from django.urls import path
from . import views
# app_name = 'smsApps'
urlpatterns = [
    path('', views.index, name='index'),
    path('categorey/', views.categoreyView, name='categorey'),
    path('addcategories/', views.addCategorey, name='addcategorey'),
    # path('save_category/',views.save_category,name='save-category'),
    # path('admin/', admin.site.urls),
]
