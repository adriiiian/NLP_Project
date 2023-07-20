from django.urls import path
from sent_analysis import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict')
]