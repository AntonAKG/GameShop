from django.urls import path, include

from .views import RegisterView, LoginClassView, ProfileView

# auth urls
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginClassView.as_view(), name='login')
]

# Profile urls
urlpatterns += [
    path('', ProfileView.as_view(), name='profile')
]
