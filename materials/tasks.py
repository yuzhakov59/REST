from datetime import timezone, timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from users.models import User


@shared_task
def send_course_update_email(user_email, course_name):
    """ Задача для отправки email пользователю об обновлении курса. """
    subject = f"Обновление курса: {course_name}"
    message = f"Здравствуйте!\n\nМатериалы курса '{course_name}', на который вы подписаны, были обновлены."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
    return f"Письмо об обновлении курса '{course_name}' отправлено на {user_email}"


def block_inactive_users():
    """
    Проверяет пользователей по дате последнего входа.
    Если пользователь не заходил более месяца, блокирует его (is_active = False).
    """
    now = timezone.now()
    one_month_ago = now - timedelta(days=30)

    inactive_users = User.objects.filter(last_login__lt=one_month_ago)

    for user in inactive_users:
        if user.is_active:
            user.is_active = False
            user.save()
    return


