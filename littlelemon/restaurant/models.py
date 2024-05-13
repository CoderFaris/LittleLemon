from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    BookingDate = models.DateField()

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self):
        return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
