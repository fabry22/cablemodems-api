from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('cablemodems/', views.CableModemList.as_view()),
    path('cablemodems/<int:pk>/', views.CableModemDetail.as_view()),
    path('cablemodems/models', views.CableModemModelsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)