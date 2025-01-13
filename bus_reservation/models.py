from django.db import models


class Bus(models.Model):
    name = models.CharField(max_length=50)
    bus_no = models.IntegerField( primary_key=True)

    class Meta:
        db_table = 'bus'  # Adjust the app_label to match your app name


class timings(models.Model):
    time = models.TimeField()
    t_no = models.CharField(max_length=30, primary_key=True)
    bus_no = models.ForeignKey('bus_reservation.Bus', on_delete=models.CASCADE)


class timings2(models.Model):
    time_s = models.TimeField()
    t_no_s = models.AutoField(primary_key=True)
    bus_no = models.ForeignKey('bus_reservation.Bus', on_delete=models.CASCADE)


class ConductorDetails(models.Model):
    cond_phone = models.CharField(max_length=15, primary_key=True)
    cond_name = models.CharField(max_length=64)
    d_name = models.CharField(max_length=64)
    bus_no = models.ForeignKey('bus_reservation.Bus', on_delete=models.CASCADE)


class Destination2(models.Model):
    location = models.CharField(max_length=64, primary_key=True)
    fee = models.CharField(max_length=15)


class Destination(models.Model):
    fee = models.CharField(max_length=15, primary_key=True)
    locaxn = models.CharField(max_length=64)


class BusStatus(models.Model):
    seat_status = models.CharField(max_length=30, primary_key=True)


class SeatExistence(models.Model):
    exist_status = models.CharField(max_length=30, primary_key=True)


class Seats(models.Model):
    seat_no = models.CharField(max_length=7, primary_key=True)
    
    
class CombinedBusData(models.Model):
    bus_name = models.CharField(max_length=50)
    bus_number = models.CharField(max_length=10)
    timing_time = models.TimeField(null=True, blank=True)
    timing_number = models.CharField(max_length=30, null=True, blank=True)
    timing2_time = models.TimeField(null=True, blank=True)
    timing2_number = models.IntegerField(null=True, blank=True)
    conductor_phone = models.CharField(max_length=15, null=True, blank=True)
    conductor_name = models.CharField(max_length=64, null=True, blank=True)
    destination_name = models.CharField(max_length=64, null=True, blank=True)
    destination_fee = models.CharField(max_length=15, null=True, blank=True)
    destination_location = models.CharField(max_length=64, null=True, blank=True)
    destination2_location = models.CharField(max_length=64, null=True, blank=True)
    destination2_fee = models.CharField(max_length=15, null=True, blank=True)
    bus_status = models.CharField(max_length=30, null=True, blank=True)
    seat_existence = models.CharField(max_length=30, null=True, blank=True)
    seat_number = models.CharField(max_length=7, null=True, blank=True)
