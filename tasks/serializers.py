from rest_framework import serializers
from .models import Event, Participant, Registration
from django.utils import timezone
from validate_email import validate_email

class Event_List_Serializer(serializers.ModelSerializer):
    # Serializer for listing events, including only the event name.
    class Meta:
        model=Event
        fields=['event_name']
        
class Event_Detail_Serializer(serializers.ModelSerializer):
    #  Serializer for detailed event information, including all fields of the Event model.
    class Meta:
        model=Event
        fields="__all__"
        
class Participant_Serializer(serializers.ModelSerializer):
    #  Serializer for detailed event information, including all fields of the Event model.
    class Meta:
        model=Participant
        fields="__all__"
        
    def validate_email(self,value):
        #   Custom validation for participant email.
        if not value:
            raise serializers.ValidationError("email is not valid")
        try:
            if Participant.objects.filter(email=value):
                raise serializers.ValidationError("email already exists")
        except Participant.DoesNotExist:
            pass
        return value

class Registration_Serializer(serializers.ModelSerializer):
    #  Serializer for event registration
    class Meta:
        model=Registration
        fields=["event","participant"]
    

    def validate_event(self,value):
        #  Custom validation for event date
        if value.event_date < timezone.now().date():
            raise serializers.ValidationError("event date has already passed")
        return value
