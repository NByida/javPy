# coding:utf-8
import json
from robotparser import Entry

from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from jav.models import Film


def index(request,a):
    entry=Film.objects.all()[20*(int(a)-1):int(a)*20]
    from django.core import serializers
    json_data = serializers.serialize('json', entry)
    json_data = json.loads(json_data)
    from django.http import HttpResponse, JsonResponse
    return JsonResponse(json_data, safe=False)

