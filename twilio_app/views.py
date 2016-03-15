from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

@twilio_view
def sms(request):
    r = Response()
    r.message('Hello world! Twilio integrated with Django')
    return r

@twilio_view
def ring(request):
    r = Response()
    r.play('http://bit.ly/phaltsw')
    return r
    
# This is a plain view that returns manually written TwiML
# Note: it's not linked to a URL in this example.
@csrf_exempt
def sms_plain(request):
    twiml = '<Response><Message>TwiML message using XML tags</Message></Response>'
    return HttpResponse(twiml, content_type='text/xml')

@csrf_exempt
def sms_without_twilio_django(request):
    r = Response()
    r.message('Hello from your Django app!')
    return HttpResponse(r.toxml(), content_type='text/xml')


# This is an example that looks for a parameter in the request
# and returns a personalised message
@twilio_view
def sms_personal(request):
    name = request.POST.get('Body', '')
    msg = 'Hey %s, how are you today?' % (name)
    
    r = Response()
    r.message(msg)
    return r