from django.shortcuts import render
from .models import club_Club
# Create your views here.

def listeClubs(request):
    clubs = club_Club.objects.order_by('dateCreation')
    return render(request, 'clubs/listeClubs.html', {'clubs': clubs})
