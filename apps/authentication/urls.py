from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from apps.authentication import views, forms

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html', form_class=forms.CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/login.html', next_page=reverse_lazy('login')),
        name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('register/', views.register, name='register')
]
