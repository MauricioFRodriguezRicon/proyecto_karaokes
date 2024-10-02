"""
URL configuration for karaoke_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('main-menu',views.main_menu,name='main-menu'),
    path('generate-karaoke',views.generate_karaoke,name='generate-karaoke'),
    path('synchronize',views.synchronize,name='synchronize'),
    #path('',views.view_collection,name='view-collection'),
    #path('karaoke/',include('karaoke.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOTa)
