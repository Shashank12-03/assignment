from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Event, Registration, Participant
from .serializers import Event_List_Serializer, Event_Detail_Serializer, Registration_Serializer, Participant_Serializer

# Create your views here.

class EventCreateView(generics.ListCreateAPIView):
    #View for creating and listing events.
    queryset=Event.objects.all() # Retrieve all events from the database
    serializer_class=Event_Detail_Serializer # Use Event_Detail_Serializer to serialize event data
    
    
class EventListView(generics.ListAPIView):
    #View for listing events.
    queryset=Event.objects.all()
    serializer_class=Event_List_Serializer # Use Event_List_Serializer to serialize event data
    
class EventDetailsView(generics.RetrieveAPIView):
    # View for retrieving details of a specific event.
    queryset=Event.objects.all()
    serializer_class=Event_Detail_Serializer 

class ParticipantView(generics.ListCreateAPIView):
    #View for listing and creating participants.
    queryset=Participant.objects.all() # Retrieve all participants from the database
    serializer_class=Participant_Serializer
    
class RegisterEventView(generics.CreateAPIView):
    #View for registering participants for events.
    serializer_class=Registration_Serializer
    
    def create(self,request, *args, **kwargs):
        #Custom create method to handle registration requests.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
