from django.urls import path
from api import views

urlpatterns = [
    path('predict', views.predict_carprice),
]