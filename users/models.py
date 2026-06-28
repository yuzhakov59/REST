from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True, help_text="Введите номер телефона")
    country = models.CharField(max_length=50, verbose_name='Страна', blank=True, null=True, help_text="Введите страну")
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name='Аватар', blank=True, null=True, help_text="Загрузите свой аватар")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email



class PaymentMethodChoices(models.TextChoices):
    CASH = 'cash', 'Наличные'
    TRANSFER = 'transfer', 'Перевод на счет'


class Payment(models.Model):
    from materials.models import Course, Lesson
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', verbose_name="Пользователь")
    date_of_payment = models.DateTimeField(default=timezone.now, verbose_name="Дата оплаты")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments', verbose_name="Оплаченный курс")
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Оплаченный урок")

    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=10, choices=PaymentMethodChoices.choices, default=PaymentMethodChoices.TRANSFER, verbose_name="Способ оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Платеж от {self.user.email} на сумму {self.amount} от {self.date_of_payment.strftime('%Y-%m-%d')}"

