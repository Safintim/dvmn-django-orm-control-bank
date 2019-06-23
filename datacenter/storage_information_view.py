from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = []
    now = timezone.now()

    for visitor in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append({
            "who_entered": visitor.passcard.owner_name,
            "entered_at": visitor.entered_at,
            "duration": now - visitor.entered_at,
        })

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
