from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    event_name=models.CharField(max_length=100)
    event_description=models.TextField()
    event_date=models.DateField()
    event_time=models.TimeField()
    
    def __str__(self):
        return self.event_name
    
class Participant(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.name

class Registration(models.Model):
    event=models.ForeignKey('Event',on_delete=models.CASCADE)
    participant=models.ForeignKey('Participant',on_delete=models.CASCADE)
    timestamp=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.participant.name} registered for event {self.event.event_name} at {self.timestamp}"
