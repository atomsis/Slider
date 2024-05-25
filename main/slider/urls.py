from django.urls import path, include
from .views import slider_view

app_name = 'slider'

urlpatterns = [
    path('', slider_view, name='slider'),
    # path('accounts/', include('allauth.urls')),
]
