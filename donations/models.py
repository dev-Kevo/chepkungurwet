from django.db import models

class DonationManager(models.Manager):
    def total_amount(self):
        return self.aggregate(total=models.Sum('amount'))['total'] or 0

class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    objects = DonationManager()

    def __str__(self):
        return f"{self.donor_name} - {self.amount}"

    @classmethod
    def total_amount(cls):
        return cls.objects.aggregate(models.Sum('amount'))['amount__sum'] or 0