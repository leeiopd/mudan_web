from django.shortcuts import render, get_object_or_404
from .models import Member, Part, MudanNo, Alive
from notices.models import Onenotice
# Create your views here.


def list(request):
    onenotice = get_object_or_404(Onenotice, pk=1)
    mudannos = MudanNo.objects.all()
    parts = Part.objects.all()
    alives = Alive.objects.all()
    if request.method == 'POST':
        search_mudanno = request.POST.get('mudanno')
        search_part = request.POST.get('part')
        search_alive = request.POST.get('alive')
        if search_mudanno == 'all' and search_part == 'all' and search_alive == 'all':
            members = Member.objects.all().order_by('-mudanNo')
        if search_mudanno != 'all' and search_part != 'all' and search_alive != 'all':
            members = Member.objects.filter(
                mudanNo_id=search_mudanno, alive_id=search_alive, part=search_part).order_by('-mudanNo')
        if search_mudanno == 'all' and search_part == 'all' and search_alive != 'all':
            members = Member.objects.filter(
                alive_id=search_alive).order_by('-mudanNo')
        if search_mudanno == 'all' and search_part != 'all' and search_alive == 'all':
            members = Member.objects.filter(
                part_id=search_part).order_by('-mudanNo')
        if search_mudanno != 'all' and search_part == 'all' and search_alive == 'all':
            members = Member.objects.filter(
                mudanNo_id=search_mudanno).order_by('-mudanNo')
        if search_mudanno == 'all' and search_part != 'all' and search_alive != 'all':
            members = Member.objects.filter(
                alive_id=search_alive, part_id=search_part).order_by('-mudanNo')
        if search_mudanno != 'all' and search_part == 'all' and search_alive != 'all':
            members = Member.objects.filter(
                alive_id=search_alive, mudanNo_id=search_mudanno).order_by('-mudanNo')
        if search_mudanno != 'all' and search_part != 'all' and search_alive == 'all':
            members = Member.objects.filter(
                mudanNo_id=search_mudanno, part_id=search_part).order_by('-mudanNo')
    else:
        last_mudanNo = MudanNo.objects.all().last()
        members = Member.objects.filter(
            mudanNo_id=last_mudanNo).order_by('-mudanNo')
    context = {'members': members, 'onenotice': onenotice,
               'mudannos': mudannos, 'parts': parts, 'alives': alives}
    return render(request, 'members/list.html', context)


def detail(request, member_pk):
    onenotice = get_object_or_404(Onenotice, pk=1)
    member = get_object_or_404(Member, pk=member_pk)
    context = {'member': member, 'onenotice': onenotice}

    return render(request, 'members/detail.html', context)
