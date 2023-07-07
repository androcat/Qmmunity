from django.urls import path
from . import views

urlpatterns = [
    path('', views.logged_in, name='logged-in')
    # path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
