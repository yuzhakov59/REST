from rest_framework import serializers
from .models import Payment, PaymentMethodChoices, User, Amount_lesson


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, instance):

        representation = super().to_representation(instance)
        representation['payment_method'] = PaymentMethodChoices(instance.payment_method).label
        return representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Amount_lessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amount_lesson
        fields = '__all__'