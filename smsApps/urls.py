from django.urls import path
from smsApps import views
app_name = 'smsApps'
urlpatterns = [
    path('', views.index, name='index'),

    # path('admin/', admin.site.urls),
]
