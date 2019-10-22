from django.shortcuts import render, get_object_or_404
from notices.models import Onenotice
from .models import Workweek, Workhour, Table, Nowteam, Nowsong

# Create your views here.


def list(request):
    onenotice = get_object_or_404(Onenotice, pk=1)
    workhours = Workhour.objects.all()
    tables = Table.objects.all()
    context = {'tables': tables,
               'workhours': workhours, 'onenotice': onenotice}
    return render(request, 'worktimes/list.html', context)


def detail(request, teamId):
    onenotice = get_object_or_404(Onenotice, pk=1)
    team = Nowteam.objects.get(pk=teamId)
    name = team.name
    members = team.members.all()
    songs = Nowsong.objects.filter(team_id=teamId)
    context = {'onenotice': onenotice, 'name': name,
               'members': members, 'songs': songs}
    return render(request, 'worktimes/detail.html', context)
