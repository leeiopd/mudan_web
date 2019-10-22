from django.shortcuts import render, get_object_or_404
from notices.models import Onenotice
from .models import Workweek, Workhour, Table, Nowteam

# Create your views here.


def list(request):
    onenotice = get_object_or_404(Onenotice, pk=1)
    workhours = Workhour.objects.all()
    tables1 = Table.objects.filter(week_id=1)
    tables2 = Table.objects.filter(week_id=2)
    tables3 = Table.objects.filter(week_id=3)
    tables4 = Table.objects.filter(week_id=4)
    tables5 = Table.objects.filter(week_id=5)
    tables6 = Table.objects.filter(week_id=6)
    tables7 = Table.objects.filter(week_id=7)
    context = {'tables1': tables1, 'tables2': tables2, 'tables3': tables3, 'tables4': tables4, 'tables5': tables5, 'tables6': tables6, 'tables7': tables7,
               'workhours': workhours, 'onenotice': onenotice}
    return render(request, 'worktimes/list.html', context)
