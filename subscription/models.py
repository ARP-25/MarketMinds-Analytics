from django.db import models

# Create your models here.
class SubscriptionPlan(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')     
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()

    def __str__(self):
        return self.title