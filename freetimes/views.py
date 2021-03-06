from django.shortcuts import render, get_object_or_404
from .models import Table, Freeweek, Freehour
from members.models import Member
from notices.models import Onenotice

# Create your views here.


def list(request):
    onenotice = get_object_or_404(Onenotice, pk=1)
    freeweeks = Freeweek.objects.all()
    freehours = Freehour.objects.all()
    tables = Table.objects.all()
    context = {'tables': tables, 'freeweeks': freeweeks,
               'freehours': freehours, 'onenotice': onenotice}
    return render(request, 'freetimes/list.html', context)


def detail(request, weekId, hourId):
    onenotice = get_object_or_404(Onenotice, pk=1)
    members = Member.objects.filter(
        member_freetimes__week__id=weekId, member_freetimes__hour__id=hourId)
    week = Freeweek.objects.get(id=weekId)
    hour = Freehour.objects.get(id=hourId)
    context = {'members': members, 'onenotice': onenotice,
               'week': week, 'hour': hour, }
    return render(request, 'freetimes/detail.html', context)
