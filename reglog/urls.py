from django.urls import path
from reglog import views
app_name = 'reglog'
urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('registration/', views.signupView, name='signup'),
    path('logout/', views.logoutView, name='logout'),
    # path('test/', views.test, name='test'),
    # path('admin/', admin.site.urls),
]
