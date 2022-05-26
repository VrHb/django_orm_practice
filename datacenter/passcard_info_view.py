from datacenter.models import Passcard, is_visit_long
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = [] 
    visits_info = Visit.objects.filter(passcard=passcard)
    for visit in visits_info:
        visit_info = {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
        passcard_visits.append(visit_info)
    
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': passcard_visits
    }
    return render(request, 'passcard_info.html', context)

