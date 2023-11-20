from django.urls import path

from .views import TestAPIView

urlpatterns = [
    path("", TestAPIView.as_view(), name="test-api-view"),
]
