from django.shortcuts import render, get_object_or_404
from notices.models import Onenotice
from .models import Workweek, Workhour, Table, Nowteam

# Create your views here.


def list(request):
    onenotice = get_object_or_404(Onenotice, pk=1)
    workhours = Workhour.objects.all()
    tables = Table.objects.all()
    context = {'tables': tables,
               'workhours': workhours, 'onenotice': onenotice}
    return render(request, 'worktimes/list.html', context)
