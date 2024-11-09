from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main_menu, name='main-menu'),
    path('generate-karaoke', views.generate_karaoke, name='generate-karaoke'),
    path('synchronize', views.synchronize, name='synchronize'),
    path('finished',views.finished,name='finished'),
    path('generating-karaoke', views.generating_karaoke, name='generating-karaoke'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
