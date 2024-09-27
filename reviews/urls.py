from django.urls import path
from reviews import views  # Ensure this is correct

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('api/sentiment-analysis/', views.sentiment_analysis, name='sentiment-analysis'),
]
