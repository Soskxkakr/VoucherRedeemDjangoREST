from django.db import models

# Create your models here.
class Voucher(models.Model):
    voucher_code = models.CharField(max_length=5)
    discount = models.CharField(max_length=15, default='0% OFF')
    no_of_use = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.voucher_code