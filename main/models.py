from django.db import models


class Booking(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    service = models.CharField(max_length=100)
    service_date = models.DateField()
    special_request = models.TextField(blank=True)

    def __str__(self):
        return f"Booking for {self.user_name} on {self.service_date}"

class RemainingItem(models.Model):
    item_name = models.CharField(max_length=100)
    remaining_quantity = models.PositiveIntegerField(default=0)
    note = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name


