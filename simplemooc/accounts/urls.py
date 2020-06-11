from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(next_page='core:home'), name='logout'),
    path('cadastre-se/', views.register, name='register'),
    path('nova-senha/', views.password_reset, name='password_reset'),
    re_path(r'^confirmar-nova-senha/(?P<key>\w+)/$',
            views.password_reset_confirm, name='password_reset_confirm'),
    path('editar/', views.edit, name='edit'),
    path('editar-senha/', views.edit_password, name='edit_password'),
]
