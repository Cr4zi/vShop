from django.shortcuts import render
from django.http import HttpResponse

import json

from .models import *


def index(request):
    res = json.dumps(["It's the index route there is nothing to be here"])
    return HttpResponse(res, content_type='text/json')
