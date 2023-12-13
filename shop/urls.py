from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import HomeView

urlpatterns = [
                  path('', HomeView.as_view(), name='home')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)