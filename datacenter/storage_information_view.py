from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import datetime


def storage_information_view(request):
    non_closed_visits = []
    now = timezone.now()

    for visit in Visit.objects.filter(leaved_at=None):
        duration = now - visit.entered_at
        non_closed_visits.append({
            "who_entered": visit.passcard.owner_name,
            "date": visit.entered_at,
            "duration": duration,
            'is_strange': duration > datetime.timedelta(minutes=60)
        })

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
