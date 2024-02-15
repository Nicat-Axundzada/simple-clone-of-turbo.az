from django.contrib import admin
from cars import models
# Register your models here.
admin.site.register(models.Car)
admin.site.register(models.Property)
admin.site.register(models.Condition)
admin.site.register(models.Ban)
admin.site.register(models.Brand)
admin.site.register(models.Model)
