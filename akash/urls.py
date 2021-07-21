
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('professional', views.professional, name='professional'),
    path('study', views.study, name='study'),
    path('search', views.search, name='search'),
    path('delete/<int:pid>', views.delete, name='delete'),
 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
