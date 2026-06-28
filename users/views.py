from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Subscription
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


class SubscriptionManageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user = request.user

        course_id = request.data.get('course_id')

        try:
            course_item = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({"detail": "Курс с указанным ID не найден."}, status=status.HTTP_404_NOT_FOUND)

        subs_item = Subscription.objects.filter(user=user, course=course_item).first()

        if subs_item:
            subs_item.delete()
            message = 'Подписка удалена.'
            status_code = status.HTTP_200_OK
        else:
            Subscription.objects.create(user=user, course=course_item, status=True)
            message = 'Подписка добавлена.'
            status_code = status.HTTP_201_CREATED
        return Response({"message": message}, status=status_code)


