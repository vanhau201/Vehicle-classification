
from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverView,name="OverView"),
    path('history/', views.History,name="History"),
    path('predict/', views.Predict,name="Predict"),
]
