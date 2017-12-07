from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from Search.models import *

from Accounts.models import Member

from Search.models import Product

appname = 'Basket'
saved_id=0;
def Home(request): # This method load up the HomePage template.

  queryset_list = Rent.objects.all()
  queryset= Slides.objects.all()
  context = {

    "object_list": queryset_list,
    "title": queryset,
  }


  return render(request, 'HomePage.html', context) # render the HomePage template

def savedidM(request, saved_id):

        print saved_id

        if 'username' in request.session:
            userid = request.session['username']
            print userid
            b = SavedItems(Display_id=saved_id, Userid=userid)
            b.save()
            return HttpResponseRedirect(reverse('Basket'))

        elif 'username' not in request.POST:

            context = {'appname': appname}
            return render(request, "Login.html", context)
        else:
            u = request.POST.get('username')
            p = request.POST.get('password')
            try:
                member = Member.objects.get(pk=u)

            except Member.DoesNotExist:
                return HttpResponse("User does not exist")
            if p == member.password:
                request.session.set_expiry(400)
                queryset0 = Member.objects.filter(username=u)
                request.session['username'] = u
                request.session['password'] = p

                return HttpResponseRedirect(reverse('Basket'))
            else:
                return HttpResponse("Wrong password")

def LinkSearch(request, q):
    queryset_list = Product.objects.all()
    queary = q
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


