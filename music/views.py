from django.shortcuts import render_to_response
from django.template import RequestContext
from music.models import Track

def player(request):
    tracks = Track.objects.all()
    return render_to_response('music/player.html', {'tracks':tracks}, context_instance=RequestContext(request))
