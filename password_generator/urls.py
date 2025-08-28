from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from passwords.views import signup, save_password

urlpatterns = [
    path('', include('passwords.urls'), name='password'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('save-password', save_password, name='save-password')
]
