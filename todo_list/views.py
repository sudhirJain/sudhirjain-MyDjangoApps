from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid:
            form.save()
            all_items = List.objects.all()
            page = request.GET.get('page', 1)

            paginator = Paginator(all_items, 5)
            try:
                    all_items = paginator.page(page)
            except PageNotAnInteger:
                    all_items = paginator.page(1)
            except EmptyPage:
                    all_items = paginator.page(paginator.num_pages)
            messages.success(request,('Item Has Been Added to List'))
            return render(request,'todo_list/home.html',{'all_items':all_items})
    else:
        all_items = List.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(all_items, 5)
        try:
                all_items = paginator.page(page)
        except PageNotAnInteger:
                all_items = paginator.page(1)
        except EmptyPage:
                all_items = paginator.page(paginator.num_pages)

        return render(request,'todo_list/home.html',{'all_items':all_items})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item Has Been Deleted'))
    return redirect('home')

def cross_off(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')
        

