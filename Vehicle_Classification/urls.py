
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('api/', include('Api.urls')),
    path('', include('Fontend.urls'))
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
