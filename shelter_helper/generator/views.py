# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Passport

def index(request):
	passport_list = Passport.objects.order_by('passport_no')[:5]
	template = loader.get_template('generator/index.html')
 	context = {
        		'passport_list': passport_list,
	}
	return HttpResponse(template.render(context, request))
def detail(request, passport_no):
    try:
        passport = Passport.objects.get(pk=passport_no)
    except Passport.DoesNotExist:
        raise Http404("Passport does not exist")
    return render(request, 'generator/detail.html', {'passport': passport})
