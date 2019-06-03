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
        if serch_mudanno != 'all':
            members = Member.objects.filter(mudanNo.pk = search_mudanno)
        else:
            members = Member.ojbects.all()
        if serch_part != 'all':
            members = members.objects.filter(part.pk = search_part)
        if serch_alive != 'all':
            members = members.ojbects.filter(alive.pk = search_alive)

    else:
        members = Member.objects.all().order_by('-mudanNo')
    context = {'members':members, 'onenotice':onenotice, 'mudannos':mudannos, 'parts':parts, 'alives':alives}
    return render(request, 'members/list.html', context)

def detail(request, member_pk):
    onenotice = get_object_or_404(Onenotice, pk=1)
    member = get_object_or_404(Member, pk=member_pk)
    context = {'member':member, 'onenotice':onenotice}

    return render(request, 'members/detail.html', context)