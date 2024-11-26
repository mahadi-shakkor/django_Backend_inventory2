from django.urls import path
from . import views

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),  # Home page route
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout route
]


