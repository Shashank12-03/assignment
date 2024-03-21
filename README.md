# Event Registration API

## Overview

This project implements a simple Event Registration API using Django and Django REST Framework. The API allows users to manage events, participants, and registrations. It provides endpoints for listing events, retrieving event details, creating events, adding participants, and registering participants for events.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- validate_email (Python package)

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Shashank12-03/assignment.git
cd <project_directory>

```
## Install required python packages using pip
pip install -r requirements.txt

## Apply migrations to create the database schema:
python manage.py migrate

## Run the Django development server:
python manage.py runserver

## Access the API endpoints at 
http://127.0.0.1:8000/

## API Endpoints
- **List Events:** `GET /event/` - Lists all available events.
- **Create Event:** `POST /events_create/` - Creates a new event.
- **Add Participant:** `POST /add_participant/` - Adds a new participant.
- **Event Details:** `GET /event/<event_id>/` - Retrieves details of a specific event.
- **Register Event:** `POST /event/register/` - Registers a participant for an event.


## Testing with Postman
- Install Postman from https://www.postman.com/downloads/.
- Import the provided Postman collection file (event_registration_api.postman_collection.json).
- Use the imported collection to test the API endpoints.
- Ensure that the server is running (python manage.py runserver) before testing the endpoints.
