from django.urls import path, include
from rest_framework.routers import DefaultRouter  # Ensure this import is here
from .views import CustomUserViewSet, DataModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Router for automatic URL routing
router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'data', DataModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
