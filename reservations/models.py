from django.db import models


class Property(models.Model):
    owner = models.ForeignKey('auth.User', related_name='properties', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    number_of_beds = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.address


class Guest(models.Model):
    owner = models.ForeignKey('auth.User', related_name='guests', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    owner = models.ForeignKey('auth.User', related_name='reservations', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='reservations', on_delete=models.CASCADE)
    guests = models.ManyToManyField(Guest, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField()

    RESERVATION_STATUSES = [
        ("REQUESTED", "Requested"),
        ("APPROVED", "Approved"),
        ("PAYED", "Payed"),
        ("CANCELED", "Canceled"),
    ]
    status = models.CharField(max_length=9, choices=RESERVATION_STATUSES)

    def __str__(self):
        return f"{self.property} - {self.start_date} - {self.end_date}"
