from django.shortcuts import render, get_object_or_404, redirect
from .models import Onenotice, Notice
from .forms import NoticeForm

# Create your views here.
def list(request):
    notices = Notice.objects.all().order_by('-pk')
    onenotice = get_object_or_404(Onenotice, pk=1)
    context = {'notices':notices, 'onenotice':onenotice}
    return render(request, 'notices/list.html', context)

def create(request):
    onenotice = get_object_or_404(Onenotice, pk=1)
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notices:list')
    else:
        form = NoticeForm()
        context = {'form':form, 'onenotice':onenotice}
    return render(request, 'notices/create.html', context)

def update(request, notice_pk):
    onenotice = get_object_or_404(Onenotice, pk=1)
    notice = get_object_or_404(Notice, pk=notice_pk)
    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notices:detail', notice_pk)
    else:
        form = NoticeForm(instance=notice)
        context = {'form':form, 'onenotice':onenotice}
    return render(request, 'notices/update.html', context)


def detail(request, notice_pk):
    onenotice = get_object_or_404(Onenotice, pk=1)
    notice = get_object_or_404(Notice, pk=notice_pk)
    context = {'notice':notice, 'onenotice':onenotice}
    return render(request, 'notices/detail.html', context)


def delete(request, notice_pk):
    notice = get_object_or_404(Notice, pk=notice_pk)
    notice.delete()
    return redirect('notices:list')


def onenotice(request):
    onenotice = get_object_or_404(Onenotice, pk=1)
    if request.method == "POST":
        onenotice.content = request.POST.get('content')
        onenotice.save()
    return redirect('notices:list')

