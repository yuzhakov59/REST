from rest_framework import serializers
from .models import Payment, PaymentMethodChoices


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        representation['payment_method'] = PaymentMethodChoices(instance.payment_method).label
        return representation

