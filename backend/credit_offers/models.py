from django.db import models


class CreditOffersModel(models.Model):
    bank_name = models.CharField(max_length=200)
    term_min = models.IntegerField()
    term_max = models.IntegerField()
    rate_min = models.FloatField()
    rate_max = models.FloatField()
    payment_min = models.IntegerField()
    payment_max = models.IntegerField()

    def __str__(self):
        return self.bank_name
