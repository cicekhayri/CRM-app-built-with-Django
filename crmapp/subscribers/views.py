from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


from .forms import SubscriberForm


def subscriber_new(request, template='subscriber/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # unpack form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            # create the user record
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            # create Subscriber Record
            # Process payment (via Stripe)
            # auto login the user
            return HttpResponseRedirect('/success/')
    else:
        form = SubscriberForm()

    return render(request, template, {'form':form})