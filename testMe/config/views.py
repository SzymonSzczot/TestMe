from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from trials.models import Test


@login_required
def home(request):
    context = {}
    # TODO replace
    #context['tests'] = Test.objects.filter(owner=request.user)
    context['tests'] = Test.objects.all
    return render(request, 'home.html', context)


@login_required
def help(request):
    return render(request, 'help.html', )


def welcome(request):
    return render(request, 'welcome.html')
