from datacenter.models import Passcard, is_visit_long
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    serialized_visits = [] 
    passcard_visits = Visit.objects.filter(passcard=passcard)
    for visit in passcard_visits:
        passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
        serialized_visits.append(passcard_visit)
    
    
    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)

