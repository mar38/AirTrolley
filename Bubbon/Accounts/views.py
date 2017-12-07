from django.shortcuts import render
from models import Member
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


appname = 'Accounts'

# This fucntion (method) is for login which is intergrated with Ajax.

def login(request):
    try:
        userid = request.session['username']
        return HttpResponseRedirect(reverse('Basket'))

    except:

        if 'username' not in request.POST:
            context = { 'appname': appname }
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

# This function (method) allow user to register

def register(request):

    try:
        userid = request.session['username']
        return HttpResponseRedirect(reverse('Search'))

    except:

        a=request.POST.get('FirstName',True)
        b=request.POST.get('LastName',True)
        u = request.POST.get('username')
        p = request.POST.get('password',True)
        q = request.POST.get('Address',True)
        d = request.POST.get('Postcode', True)
        n = request.POST.get('Contact', True)

        if u:
            if p:
                user = Member(First_Name=a,Last_Name=b,username=u, password=p, Address=q, PostCode=d, Contact=n)
                user.save()
                return HttpResponseRedirect(reverse('login'))

        context = {
            'appname': appname,
            'username' : u
        }
        return render(request, "Registration.html", context)

# This fucntion (method) check if the user is already in the session.

def loggedin(f):
    def test(request):
        if 'username' in request.session:
            return f(request)
        else:
            return render(request, 'Success-to-Search.html', {})
    return test

# This fucntion (method) check if the user already exit or not.

def logCheckUser(request):

    print 'came to logcheckuser'

    if 'username' in request.POST:
        u = request.POST['username']
        try:
            member = Member.objects.get(username=u)
            print member
            return HttpResponse("<span class='available'>&nbsp;&#x2714; Valid username</span>")

        except Member.DoesNotExist:
            return HttpResponse("<span class='taken'>&nbsp;&#x2718; Unknown username</span>")
    else:
        return HttpResponse("")