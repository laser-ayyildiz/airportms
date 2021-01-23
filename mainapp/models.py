from django.db import models

class Airport(models.Model):
    airport_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField(primary_key=True, max_length=250)
    contact_number = models.CharField(max_length=30)

    class Meta:
        unique_together = ('company_name', 'contact_number')

class Airplane_Manufacturer(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, default="", editable=False, related_name='airplane_manufacturer_company')
    contact_number = models.ForeignKey(Company, on_delete=models.CASCADE, default="", editable=False, related_name='airplane_manufacturer_contact')
    def __str__(self):
        return self.company_name

    class Meta:
        unique_together = ('company_name', 'contact_number')

class Airline(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, default="", editable=False, related_name='airline_company')
    contact_number = models.ForeignKey(Company, on_delete=models.CASCADE, default="", editable=False, related_name='airline_contact')
    using_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='airline_using_ap')
    def __str__(self):
        return self.company_name

    class Meta:
        unique_together = ('company_name', 'contact_number')

class Flight(models.Model):
    flight_number = models.CharField(primary_key=True, max_length=20)
<<<<<<< HEAD
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name='flight_airline')
=======
    airline = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='flight_airline')
>>>>>>> 9d19a3f3c702a7adfb9f9b42c75e9c4c04e97ab4
    weekdays = models.CharField(max_length=120)

    def __str__(self):
        return str(self.flight_number)


class Flight_Leg(models.Model):
    id = models.AutoField(primary_key=True)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_flight_number')
    leg_number = models.CharField(max_length=20)
    departure_airport_code = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='flight_departure_ac')
    scheduled_departure_time = models.TimeField()
    arrival_airport_code = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='flight_arrival_ac')
    scheduled_arrival_time = models.TimeField()

    def __str__(self):
        return str(self.flight_number) + "." + str(self.leg_number)

    class Meta:
        unique_together = ('flight_number', 'leg_number')

class Airplane_Type(models.Model):
    airplane_type_name = models.CharField(primary_key=True, max_length=50)
    max_seats = models.IntegerField()
<<<<<<< HEAD
    company = models.ForeignKey(Airplane_Manufacturer, on_delete=models.CASCADE, related_name='airplane_company')
=======
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='airplane_company')
>>>>>>> 9d19a3f3c702a7adfb9f9b42c75e9c4c04e97ab4

class Airplane(models.Model):
    airplane_id = models.CharField(primary_key = True,max_length=10)
    total_number_of_seats = models.IntegerField()
    airplane_type = models.ForeignKey(Airplane_Type, on_delete=models.CASCADE, related_name='airplane_airplane_type')

class Leg_Instance(models.Model):
    id = models.AutoField(primary_key=True)
    flight_number = models.ForeignKey(Flight_Leg, on_delete=models.CASCADE, related_name='legInstance_flight_number')
    leg_number = models.ForeignKey(Flight_Leg, on_delete=models.CASCADE, related_name='legInstance_leg_number')
    date = models.DateField()
    number_of_available_seats = models.IntegerField()
    airplane_id = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='ap_id')
    departure_airport_code = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='legInstance_aparture_ac')
    departue_time = models.TimeField()
    arrival_arport_code = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='legInstance_arrival_ac')
    arrival_time = models.TimeField()

    def __str__(self):
        return str(self.flight_number) + "." + str(self.leg_number) + "/" + str(self.date)

    class Meta:
        unique_together = ('flight_number', 'leg_number', 'date')

class Fare(models.Model):
    id = models.AutoField(primary_key=True)
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='fare_flight_number')
    fare_code = models.CharField(max_length=10)
    amount = models.IntegerField()
    restrictions = models.TextField()
    class Meta:
        unique_together = ('flight_number','fare_code')

    def __str__(self):
        return self.flight_number+"."+str(self.fare_code)+":"+str(self.amount)

class Customer(models.Model):
<<<<<<< HEAD
    id = models.AutoField(primary_key=True, default="")
    passport_number = models.CharField(max_length=30)
    country = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=16)
    address = models.TextField()
    email = models.CharField(max_length=150)
    def __str__(self):
        return self.customer_name

    class Meta:
        unique_together = ('passport_number', 'country')

class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    flight_number = models.ForeignKey(Leg_Instance, on_delete=models.CASCADE, related_name='seat_flight_number')
    leg_number = models.ForeignKey(Leg_Instance, on_delete=models.CASCADE, related_name='seat_leg_number')
    date = models.ForeignKey(Leg_Instance, on_delete=models.CASCADE, related_name='seat_date')
    seat_number = models.IntegerField()
    passport_number = models.ForeignKey(Customer, on_delete=models.CASCADE, default="", related_name='customer_passport_number')
    country = models.ForeignKey(Customer, on_delete=models.CASCADE, default="", related_name='customer_country')

    def __str__(self):
        return str(self.flight_number) + "." + str(self.leg_number) + "." + str(self.seat_number)

    class Meta:
        unique_together = ('flight_number', 'leg_number', 'date', 'seat_number')

class FFC(models.Model):
    id = models.AutoField(primary_key=True)
=======
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=16)
    passport_number = models.ForeignKey(Fare, on_delete=models.CASCADE, related_name='customer_passport_number')
    country = models.ForeignKey(Fare, on_delete=models.CASCADE, related_name='customer_country')
    address = models.TextField()
    email = models.CharField(max_length=150)
    class Meta:
        unique_together = ('passport_number', 'country')

    def __str__(self):
        return self.customer_name

class FFC(models.Model):
    id = models.AutoField(primary_key = True)
>>>>>>> 9d19a3f3c702a7adfb9f9b42c75e9c4c04e97ab4
    passport_number = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ffc_passport_number')
    milleage = models.IntegerField()
    country = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='ffc_country')

    class Meta:
        unique_together = ('passport_number', 'country')

    def __str__(self):
        return self.passport_number
<<<<<<< HEAD
=======


class Seat(models.Model):
    flight_number = models.ForeignKey(Leg_Instance, on_delete=models.CASCADE, related_name='seat_flight_number')
    leg_number = models.ForeignKey(Leg_Instance, on_delete=models.CASCADE, related_name='seat_leg_number')
    date = models.ForeignKey(Leg_Instance, on_delete=models.CASCADE, related_name='seat_date')
    seat_number = models.IntegerField()
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='seat_customer_name')

    def __str__(self):
        return str(self.flight_number) + "." + str(self.leg_number) + "." + str(self.seat_number)
>>>>>>> 9d19a3f3c702a7adfb9f9b42c75e9c4c04e97ab4
