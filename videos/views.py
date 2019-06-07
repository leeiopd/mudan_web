from django.shortcuts import render, get_object_or_404
from .models import Video, Year, Concert, Team
from notices.models import Onenotice
# Create your views here.

def list(request):
    onenotice  = get_object_or_404(Onenotice, pk=1)
    years = Year.objects.all()
    concerts = Concert.objects.all()
    teams = Team.objects.all()

    if request.method == 'POST':
        search_year = request.POST.get('search_year')
        search_concert = request.POST.get('search_concert')
        search_team = request.POST.get('search_team')
        if search_year == 'all' and search_concert == 'all' and search_team == 'all':
            videos = Video.objects.all()
        if search_year != 'all' and search_concert != 'all' and search_team != 'all':
            videos = Video.objects.filter(year_id = search_year, concert_id = search_concert, team_id = search_team).order_by('-year')

        if search_year != 'all' and search_concert == 'all' and search_team == 'all':
            videos = Video.objects.filter(year_id = search_year)
        if search_year == 'all' and search_concert != 'all' and search_team == 'all':
            videos = Video.objects.filter(concert_id = search_concert)
        if search_year == 'all' and search_concert == 'all' and search_team != 'all':
            videos = Video.objects.filter(team_id = search_team)

        if search_year != 'all' and search_concert != 'all' and search_team == 'all':
            videos = Video.objects.filter(year_id = search_year, concert_id = search_concert)
        if search_year == 'all' and search_concert != 'all' and search_team != 'all':
            videos = Video.objects.filter(concert_id = search_concert, team_id = search_team)
        if search_year != 'all' and search_concert == 'all' and search_team != 'all':
            videos = Video.objects.filter(team_id = search_team, year_id = search_year)

    else:
        videos = Video.objects.all()

    context = {'onenotice': onenotice, 'videos':videos, 'teams':teams, 'years':years, 'concerts':concerts}
    return render(request, 'videos/list.html', context)

def watch(request, video_pk):
    onenotice  = get_object_or_404(Onenotice, pk=1)
    video = get_object_or_404(Video, pk=video_pk)

    context = {'onenotice': onenotice, 'video':video}
    return render(request, 'videos/watch.html', context)

def detail(request, team_pk):
    onenotice  = get_object_or_404(Onenotice, pk=1)
    team = get_object_or_404(Team, pk=team_pk)
    members = team.team_members.all()
    videos = team.video_set.all().order_by('-year')

    context = {'onenotice': onenotice, 'team':team, 'videos':videos, 'members':members}
    return render(request, 'videos/detail.html', context)