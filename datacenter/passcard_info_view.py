from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import datetime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        data_visit = {
            'entered_at': visit.entered_at,
            'is_strange': False,
            'duration': timezone.now() - visit.entered_at
        }
        if visit.leaved_at:
            data_visit['duration'] = visit.leaved_at - visit.entered_at

        if is_visit_long(visit):
            data_visit['is_strange'] = True

        this_passcard_visits.append(data_visit)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


def is_visit_long(visit, minutes=60):
    if visit.leaved_at:
        return visit.leaved_at - visit.entered_at > datetime.timedelta(minutes=minutes)
    else:
        return timezone.now() - visit.entered_at > datetime.timedelta(minutes=minutes)
