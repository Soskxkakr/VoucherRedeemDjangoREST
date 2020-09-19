from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Voucher(models.Model):
    voucher_code = models.CharField(max_length=5)
    discount = models.IntegerField(
        default=0, 
        validators=[MaxValueValidator(100), MinValueValidator(0)]
        )
    no_of_use = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.voucher_code