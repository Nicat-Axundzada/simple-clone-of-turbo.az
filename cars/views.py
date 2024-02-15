from django.shortcuts import render
from django.db.models import Count
from django.views import View
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Car, Condition, Ban


class IndexView(View):
    def get(self, request):

        # Function to format the created_at datetime
        def format_created_at(created_at):
            today = timezone.now().date()
            yesterday = today - timedelta(days=1)
            if created_at.date() == today:
                return created_at.strftime("Today %H:%M")
            elif created_at.date() == yesterday:
                return created_at.strftime("Yesterday %H:%M")
            else:
                return created_at.strftime("%d,%m,%Y %H:%M")

        # Retrieve filter parameters from the request
        brand = request.GET.getlist("brand")
        model = request.GET.getlist("selected-model")
        city = request.GET.getlist("selected-city")
        currency = request.GET.getlist("selected-currency")
        ban = request.GET.getlist("selected-ban")
        is_credit = request.GET.get('credit', False)
        is_barter = request.GET.get('barter', False)
        min_price = request.GET.get('min-price')
        max_price = request.GET.get('max-price')
        # Implement Filtering
        cars = Car.objects.all()

        if brand:
            cars = cars.filter(brand__brand__in=brand)

        if model:
            cars = cars.filter(model__model__in=model)

        if city:
            cars = cars.filter(conditions__city__in=city)

        if currency:
            cars = cars.filter(conditions__currency__in=currency)
            print(cars)

        if ban:
            cars = cars.filter(ban__type__in=ban)

        if is_credit == "true":
            cars = cars.filter(conditions__credit=True)

        if is_barter == "true":
            cars = cars.filter(conditions__barter=True)

        if min_price:
            cars = cars.filter(properties__price__gte=min_price)

        if max_price:
            cars = cars.filter(properties__price__lte=max_price)

        car_instances = []
        for car in cars:
            car_instance = {
                "brand": car.brand.brand,
                "model": car.model.model,
                "ban": car.ban.type if car.ban else None,
                "properties": {
                    "image": car.properties.image.url,
                    "price": car.properties.price,
                    "year": car.properties.year,
                    "color": car.properties.color,
                    "fuel_type": car.properties.fuel_type,
                    "transmitter": car.properties.transmitter,
                    "gear_box": car.properties.gear_box,
                    "volume": float(car.properties.volume),
                    "power": car.properties.power,
                    "number_of_seats": car.properties.number_of_seats,
                    "assembled_market": car.properties.assembled_market,
                },
                "conditions": {
                    "is_new": car.conditions.is_new,
                    "is_driven": car.conditions.is_driven,
                    "city": car.conditions.city,
                    "currency": car.conditions.currency,
                    "barter": car.conditions.barter,
                    "credit": car.conditions.credit,
                    "crash": car.conditions.crash,
                    "colored": car.conditions.colored,
                    "mileage": car.conditions.mileage,
                    "salon": car.conditions.salon,
                    "personal": car.conditions.personal,
                    "number_of_owners": car.conditions.number_of_owners,
                    "broken": car.conditions.broken,
                    "status": car.conditions.status,
                    "alloy_wheels": car.conditions.alloy_wheels,
                    "ABS": car.conditions.ABS,
                    "hatch": car.conditions.hatch,
                    "rain_sensor": car.conditions.rain_sensor,
                    "central_locking": car.conditions.central_locking,
                    "park_radar": car.conditions.park_radar,
                    "air_conditioner": car.conditions.air_conditioner,
                    "seat_heating": car.conditions.seat_heating,
                    "leather_salon": car.conditions.leather_salon,
                    "xenon_lamps": car.conditions.xenon_lamps,
                    "rear_view_camera": car.conditions.rear_view_camera,
                    "side_curtains": car.conditions.side_curtains,
                    "seat_ventilation": car.conditions.seat_ventilation,
                    "created_at": format_created_at(car.conditions.created_at),
                },
            }
            car_instances.append(car_instance)

        brand_counts = list(Car.objects.values(
            'brand__brand').annotate(count=Count('brand')))
        unique_cities = list(Condition.objects.values_list(
            'city', flat=True).distinct())
        models = list(Car.objects.values_list(
            'brand__brand', 'model__model').distinct())
        currencies = [currency[0] for currency in Condition.CHOICES]
        bans = list(Ban.objects.values_list('type', flat=True).distinct())
        today = datetime.now().date()
        today_added = len(Car.objects.filter(created_at__date=today))

        content = {
            "car_instances": car_instances,
            "brand_counts": brand_counts,
            "cities": unique_cities,
            "models": models,
            "currencies": currencies,
            "bans": bans,
            "today_added": today_added,
        }

        content_json = {
            "brand_counts": brand_counts,
            "cities": unique_cities,
            "models": [{"brand": model[0], "model": model[1]} for model in models],
            "currencies": currencies,
            "bans": bans,
            "today_added": today_added,
        }
        data = {
            "content": content,
            "content_json": content_json,
        }

        return render(request, "cars/index.html", data)
