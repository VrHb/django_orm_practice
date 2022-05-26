from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):
    serialized_visits = []
    open_visits = Visit.objects.filter(leaved_at=None)
    for visit in open_visits:
        visiter = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit))
        }
        serialized_visits.append(visiter)

    context = {
        'non_closed_visits': serialized_visits,  
    }
    return render(request, 'storage_information.html', context)

