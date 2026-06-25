from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView

from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer
from users.payment.filters import PaymentFilter


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filter_class = PaymentFilter

    def get_queryset(self):
        """
        Переопределяем get_queryset для фильтрации платежей по текущему пользователю.
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


