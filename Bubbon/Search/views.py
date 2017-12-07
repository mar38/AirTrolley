from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import HttpResponse
from models import Product
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

def Search(request):
    queryset_list = Product.objects.all()
    queary = request.GET.get('q')
    if queary:
        queryset_list = queryset_list.filter(type__icontains=queary)

    paginator = Paginator(queryset_list, 20)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "list"
    }
    return render(request, 'Search.html', context)
