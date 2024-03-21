from django.urls import path
from .views import EventCreateView, EventListView, EventDetailsView, RegisterEventView, ParticipantView

urlpatterns = [
    path('event/', EventListView.as_view(), name='event-list'),  # URL pattern for listing events
    path('events_create/', EventCreateView.as_view(), name='create-event'),  # URL pattern for creating events
    path('add_participant/', ParticipantView.as_view(), name='add-participant'),  # URL pattern for adding participants
    path('event/<int:pk>/', EventDetailsView.as_view(), name='event-detail'),  # URL pattern for retrieving details of a specific event
    path('event/register/', RegisterEventView.as_view(), name='register-event'),  # URL pattern for registering participants for events
]
