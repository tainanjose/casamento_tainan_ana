
from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShowHomeView.as_view(), name='core.showhome'),
]
