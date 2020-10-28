from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/', views.docsisupdate_list),
    path('api/<int:pk>/', views.docsisupdate_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)