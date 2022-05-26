from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visiter: Visit) -> int:
    if visiter.leaved_at:
        delta = (visiter.leaved_at - visiter.entered_at).total_seconds()
        return delta
    delta = (localtime() - visiter.entered_at).total_seconds()
    return int(delta)

    
def format_duration(duration: int) -> str:
    duration_hours = int(duration // 3600)
    duration_minutes = int(duration % 3600 // 60)
    return f"{duration_hours}:{duration_minutes}:00"


def is_visit_long(visit: Visit, minutes=60) -> bool:
    visit_in_minutes = get_duration(visit) // 60
    if visit_in_minutes > minutes:
        return True
    return False

