from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from LotAPI.settings import EMAIL_HOST_USER



CHOIСES = ((True, 'Активный'),(False, 'Завершенный'))

class Lot(models.Model):
    class Meta:
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'

    lot_author = models.ForeignKey('auth.User', verbose_name='Создатель')
    lot_name = models.CharField(max_length=50, verbose_name='Название лота', blank=False)
    lot_price = models.BigIntegerField(verbose_name='Цена', blank=False)
    lot_price_step = models.IntegerField(verbose_name='Шаг цены', blank=False)
    lot_text = models.TextField(verbose_name='Описание лота', max_length=200, blank=False)
    lot_status = models.BooleanField(choices=CHOIСES, default=True, verbose_name='Статус')

    def __str__(self):
        return "%s" % self.lot_name

class Bet(models.Model):

    class Meta:
        verbose_name = 'Ставка'
        verbose_name_plural = 'Ставки'

    bet_author = models.ForeignKey('auth.User', verbose_name='Автор ставки')
    bet_on_lot = models.ForeignKey(Lot, verbose_name='Выберите лот для ставки')
    bet_sum = models.IntegerField(verbose_name='Сумма ставки', blank=False)

    def __str__(self):
        return "%s" %self.bet_author


def list_emails():
    List_email_users = []

    for user in User.objects.all():
        List_email_users.append(user.email)

    return List_email_users


def unique(objects):

    seen = set()
    unique_group = []

    for obj in objects:

        if obj.bet_author.email in seen:
            continue

        seen.add((obj.bet_author.email))
        unique_group.append(obj.bet_author.email)

    return unique_group



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Lot)
def mail_send_newLot(sender, instance, created=False, **kwargs):
    if created and instance.lot_status == True:
        send_mail('Новые торги',
                  'Начались новые торги под названием {0}'.format(instance.lot_name), EMAIL_HOST_USER,
                  list_emails(),
                  fail_silently=False)


@receiver(post_save, sender=Bet)
def mail_send_newBet(sender, instance, created=False, **kwargs):
    if created:
        emails = unique(Bet.objects.filter(bet_on_lot=instance.bet_on_lot))

        send_mail('Изменение цены',
                  'Цена аукциона под названием {0} изменена, на данный момент цена составляет: {1}'.format(instance.bet_on_lot,instance.bet_sum),
                  EMAIL_HOST_USER, emails)



