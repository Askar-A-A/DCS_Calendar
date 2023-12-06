from django.db import models

from accounts.models import User
from calendarapp.models import Event, EventAbstract, Team


class EventMember(EventAbstract):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_members"
    )
    email = models.EmailField(default='email@gmail.com')
    nickname = models.CharField(max_length=100, default='name')
    role = models.CharField(max_length=100, default='role')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members", null=True, blank=True)

    class Meta:
        unique_together = ('event', 'team', 'role')

    def __str__(self):
        return f"{self.user} - {self.role}"
