import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import sentry_sdk

from . import database
from .models import PageView

# Create your views here.
sentry_sdk.init("http://31f15e37dab5491599fa05bfa996e42f@glitchtip-demo-deepshar-glitchtip.apps.deepshar-glitch.bw5s.s1.devshift.org/3")

def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    division_by_zero = 1 / 0

    # print(division_by_zero)
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(PageView.objects.count())
