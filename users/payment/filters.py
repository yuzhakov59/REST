from django_filters import rest_framework as filters

from users.models import Payment, PaymentMethodChoices


class PaymentFilter(filters.FilterSet):

    date_of_payment__gte = filters.DateTimeFilter(field_name='date_of_payment', lookup_expr='gte')
    date_of_payment__lte = filters.DateTimeFilter(field_name='date_of_payment', lookup_expr='lte')

    course = filters.NumberFilter(field_name='course_id')
    lesson = filters.NumberFilter(field_name='lesson_id')

    payment_method = filters.ChoiceFilter(choices=PaymentMethodChoices.choices)

    class Meta:
        model = Payment
        fields = ['date_of_payment__gte', 'date_of_payment__lte', 'course', 'lesson', 'payment_method']

