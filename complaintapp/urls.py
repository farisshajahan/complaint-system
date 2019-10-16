from django.urls import path
from . import views

urlpatterns = [
        path('', views.ComplaintView.as_view(), name="main_view"),
]
