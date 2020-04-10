from django.urls import path
from core.views import HomPageView

urlpatterns = [
    path('', HomPageView.as_view(), name="home"),
]