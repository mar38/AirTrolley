
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# This method shows all the product that user added to the cart (basket)
from Search.models import Product, SavedItems


def Basket(request):

        userid = request.session['username']

        if 'username' in request.session:
            userid = request.session['username']
        queryset0 = SavedItems.objects.all().filter(Userid=userid).values('Display_id')
        queryset_list=Product.objects.filter(id__in=queryset0)

        paginator = Paginator(queryset_list, 100)
        page = request.GET.get('page')
        try:
            list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            list = paginator.page(paginator.num_pages)
        context = {

            "Basket": list,
        }
        return render(request, 'Basket.html', context)

def remove(request, Display_id):

    if 'username' in request.session:
        userid = request.session['username']
    SavedItems.objects.filter(Display_id=Display_id, Userid=userid).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




