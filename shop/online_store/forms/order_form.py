from django import forms

from ..models.validators import phone_validator


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label='Количество', min_value=1, initial=1)


class CartForm(forms.Form):
    name = forms.CharField(label='ФИО')
    address = forms.CharField(label='Адрес доставки')
    phone = forms.CharField(label='Телефон для связи', validators=[phone_validator])
    comment = forms.CharField(
        label='Комментария для продавца',
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 30})
    )

