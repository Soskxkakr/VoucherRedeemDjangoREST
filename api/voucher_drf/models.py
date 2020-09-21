from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Voucher Model/Object
class Voucher(models.Model):
    voucher_code = models.CharField(max_length=5)
    discount = models.IntegerField(
        default=0, 
        validators=[MaxValueValidator(100), MinValueValidator(0)]
        )
    no_of_use = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.voucher_code

    def saveDb(self):
        pass

    def setVoucherCode(self, voucher_code):
        self.voucher_code = voucher_code

    def setDiscount(self, discount):
        self.discount = discount

    def setNoOfUse(self, no_of_use):
        self.no_of_use = no_of_use

    def getVoucherCode(self):
        return self.voucher_code

    def getDiscount(self):
        return self.discount

    def getNoOfUse(self):
        return self.no_of_use