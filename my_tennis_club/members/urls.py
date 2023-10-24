from django.urls import path
from . import views

urlpatterns = [
    # path(url, view that handle it, app name)
    path('members/', views.members, name='members'),
]
