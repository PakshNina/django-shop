from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(label='Количество', min_value=1, initial=1)
