from django import forms

from .models import Voucher

# Voucher Form, to be displayed in the HTML page
class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = ('voucher_code',)
    