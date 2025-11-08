
from django.contrib import admin
from django.urls import path, include
from apps.colaboradores.views import HomeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("colaboradores/", include("apps.colaboradores.urls")),
    path("api/", include("apps.colaboradores.api_urls")),
    # Home: renderiza template simples em vez de redirecionar
    path("", HomeView.as_view(), name='home'),
    path('epi/', include('epi.urls')),
    path('emprestimos/', include('emprestimos.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
