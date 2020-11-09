from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import APIHomeView
from rest_framework_jwt.views import obtain_jwt_token
from clone.views import index

urlpatterns = [
    path('', index, name='index'),
    path('staff/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/upload/', include(('clone.api.urls', 'clone'), namespace='clone')),
    path('api/', APIHomeView.as_view(), name='home_api'),
    path('api-token-auth/', obtain_jwt_token, name='jwt_token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

