from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from forum import CheckoutForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


# This fuction (method) send email to user email address once they filled the checkout form.
def Checkout(request):



    return render(request, 'Checkout.html')







