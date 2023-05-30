from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 14)]


class CartAddProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['empty_label'] = ''

    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, label='', coerce=int)
    update = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)

