from django.urls import path
from clone.api import views

urlpatterns = [
    path('image/', views.Index.as_view(), name='api_create'),
]
