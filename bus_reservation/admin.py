from django.contrib import admin
from .models import Bus, timings,timings2, ConductorDetails, Destination, BusStatus, SeatExistence, Seats, CombinedBusData


admin.site.register(Bus)
admin.site.register(timings)
admin.site.register(timings2)
admin.site.register(ConductorDetails)
admin.site.register(Destination)
admin.site.register(BusStatus)
admin.site.register(SeatExistence)
admin.site.register(Seats)
admin.site.register(CombinedBusData)
