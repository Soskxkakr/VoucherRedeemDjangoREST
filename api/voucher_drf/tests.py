from django.test import TestCase

from .models import Voucher
# Create your tests here.

class VoucherTestCase(TestCase):
    def setUp(self):
        Voucher.objects.create(voucher_code="DAFG4", discount=50, no_of_use=2)
        Voucher.objects.create(voucher_code="ASXT4", discount=32, no_of_use=3)
        

    def test_voucher_code_validity(self):
        """ Test that a voucher code is eligible and exists """
        voucher1 = Voucher.objects.get(voucher_code="DAFG4")
        voucher2 = Voucher.objects.get(voucher_code="ASXT4")
        self.assertEqual(voucher1.voucher_code, "DAFG4")
        self.assertEqual(voucher2.voucher_code, "ASXT4")

    def test_update_voucher_code(self):
        voucher1 = Voucher.objects.get(voucher_code="DAFG4")
        voucher1.setDiscount(90)
        self.assertEqual(voucher1.discount, 90)


