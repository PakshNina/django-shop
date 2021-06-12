from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def phone_validator(value):
    is_matched = re.match("(?:\+7|8)\d+", value)
    if not is_matched:
        raise ValidationError(
            _('%(value)s не телефонный номер!'),
            params={'value': value},
        )
