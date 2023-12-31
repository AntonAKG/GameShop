from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import HomeView, DetailGameView, About

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('game/<int:pk>/', DetailGameView.as_view(), name='game_detail'),
    path('about/', About.as_view(), name='about')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
