from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('branch/', views.BranchView.as_view()),
    path('MultiBranchFilter/', views.MultiBranchFilter.as_view())
]
