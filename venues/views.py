from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render

from venues.models import Venue

import json

# Create your views here.
def venue_list(request):
    all_venues = Venue.objects.all()
    all_venues_json = serializers.serialize('json', all_venues)

    return HttpResponse(all_venues_json, content_type='application/json')
