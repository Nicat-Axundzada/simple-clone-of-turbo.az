from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Brand(models.Model):
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.brand


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=30)

    def __str__(self):
        return self.model


class Property(TimeStampedModel):

    class Meta:
        verbose_name_plural = "Properties"

    FUEL_CHOICES = (
        ("Benzin", "Benzin"),
        ("Diesel", "Dizel"),
        ("Gas", 'Qaz'),
        ("Electro", "Elektro"),
        ("Hybrid", "Hibrid"),
        ("Plug-in Hybrid", "Plug-in Hibrid"),
    )
    TRANSMITTER_CHOICES = (
        ('Back', "Arxa"),
        ('Front', "Ön"),
        ("Full", "Tam"),
    )

    GEAR_BOX_CHOICES = (
        ("Mechanic", "Mexaniki"),
        ("Automat", "Avtomat"),
        ("Robotized", "Robotlaşdırılmış"),
        ("Variator", "Variator"),
    )

    NUMBER_OF_SEATS_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8+", "8+"),
    )
    image = models.ImageField(upload_to='car_image/', null=True)
    price = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=12)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmitter = models.CharField(max_length=12, choices=TRANSMITTER_CHOICES)
    gear_box = models.CharField(max_length=20, choices=GEAR_BOX_CHOICES)
    volume = models.DecimalField(decimal_places=1, max_digits=3)
    power = models.IntegerField()
    number_of_seats = models.CharField(
        max_length=5, choices=NUMBER_OF_SEATS_CHOICES, null=True, blank=True)
    assembled_market = models.CharField(max_length=20, null=True, blank=True)


class Condition(TimeStampedModel):
    CHOICES = (
        ('AZN', 'AZN'),
        ('USD', 'USD'),
        ('EURO', 'EURO'),
    )
    STATUS_CHOICES = (
        (1, "Satışdadır"),
        (2, "Sifarişlə"),
    )
    is_new = models.BooleanField()
    is_driven = models.BooleanField()
    city = models.CharField(max_length=30)
    currency = models.CharField(max_length=10, choices=CHOICES)
    barter = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    crash = models.BooleanField(default=False)
    colored = models.BooleanField(default=False)
    mileage = models.IntegerField()
    salon = models.BooleanField()
    personal = models.BooleanField()
    number_of_owners = models.IntegerField(null=True, blank=True)
    broken = models.BooleanField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    alloy_wheels = models.BooleanField()
    ABS = models.BooleanField()
    hatch = models.BooleanField()  # Lyuk
    rain_sensor = models.BooleanField()
    central_locking = models.BooleanField()  # Mərkəzi qapanma
    park_radar = models.BooleanField()
    air_conditioner = models.BooleanField()
    seat_heating = models.BooleanField()
    leather_salon = models.BooleanField()
    xenon_lamps = models.BooleanField()
    rear_view_camera = models.BooleanField()
    side_curtains = models.BooleanField()
    seat_ventilation = models.BooleanField()


class Ban(TimeStampedModel):
    type = models.CharField(max_length=30)


class Car(TimeStampedModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    properties = models.ForeignKey(Property, on_delete=models.CASCADE)
    conditions = models.ForeignKey(Condition, on_delete=models.CASCADE)
    ban = models.ForeignKey(Ban, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand}-{self.model}"
