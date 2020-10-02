from django.http import HttpResponse, QueryDict
from app.models import Car
from django.template import loader
from django.views.generic import ListView
from django.db.models import Q


class CarList(ListView):
    model = Car
    template_name = 'index.html'


def car_list(request):
    template = loader.get_template('index.html')

    if len(request.GET) > 0:
        c = request.GET
        cars = Car.objects.filter(Q(manufacture=c.get('manufacture', ''))
                                & Q(model_auto=c.get('model_auto', ''))
                                & Q(year=c.get('year', 0))
                                & Q(transmission=c.get('transmission', 0))
                                & Q(color=c.get('color', '')))
        if len(cars) == 0:
            context = {
                "title": "Cars",
                "message": "Ничего не найдено по запросу",
                "cars": [],
            }
            return HttpResponse(template.render(context, request))
        else:
            context = {
                "title": "Cars",
                "cars": cars,
            }
            return HttpResponse(template.render(context, request))
    else:
        cars = Car.objects.all()
        context = {
            "title": "Cars",
            "cars": cars,
        }
        return HttpResponse(template.render(context, request))
