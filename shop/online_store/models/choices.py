class OrderStatuses:
    CREATED = 'created'
    CONFIRMED = 'confirmed'
    FINISHED = 'finished'
    CANCELED = 'canceled'


ORDERS_STATUS_CHOICES = (
    (OrderStatuses.CREATED, 'Создан'),
    (OrderStatuses.CONFIRMED, 'Подтвержден'),
    (OrderStatuses.FINISHED, 'Доставлен'),
    (OrderStatuses.CANCELED, 'Отменен')
)
