from django.urls import path, include
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from users.views import PaymentViewSet, UserCreateAPIView, SubscriptionManageView

app_name = UsersConfig.name

router = routers.DefaultRouter()

router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('api/subscriptions/manage/', SubscriptionManageView.as_view(), name='subscription-manage'),
]

