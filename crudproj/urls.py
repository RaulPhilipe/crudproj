"""crudproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/all/', views.list_all_movies),
    path('movie/user/', views.list_user_movies),
    path('movie/detail/<id>/', views.movie_detail),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('movie/register/', views.register_movie),
    path('movie/register/submit', views.set_movie),
    path('movie/delete/<id>/', views.delete_movie),
    path('', RedirectView.as_view(url='movie/all/')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
