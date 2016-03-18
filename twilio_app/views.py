from django.shortcuts import render
from django.shortcuts import redirect
# import settings to access Twilio keys
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

# for making a call
from twilio.rest import TwilioRestClient

# strip out the Twilio-specific POST parameters from a Django HttpRequest 
#   object and present them back as a TwilioRequest object
from django_twilio.request import decompose


@twilio_view
def sms(request):
    if request.method == 'GET':
        return HttpResponse("You are using GET. Use POST to communicate via SMS.")

    body = request.POST.get('Body', '')
    body = body.lower()

    if "call me" in body:

        client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN) 
    
        call = client.calls.create(
            to="978-382-3789",
            from_="19782917626",
            url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
            # monkey mp3 below doesn't work for some reason -> Application error
            # https://demo.twilio.com/hellomonkey/monkey.mp3


        msg = "I'll call you in a sec......"
        r = Response()
        r.message(msg)
        return r


    msg = 'How are you today? This is what you sent me: %s' % (body)
    # msg = 'Hello world! Twilio integrated with Django!!!'
    r = Response()
    r.message(msg)
    return r

# plays a mp3 file if you set this as voice url on Twilio
@twilio_view
def ring(request):
    r = Response()
    # r.play('http://bit.ly/phaltsw')
    r.play('https://demo.twilio.com/hellomonkey/monkey.mp3')
    return r

# takes in input from user and redirects them to handle_response view
@twilio_view
def gather_digits(request):

    msg = 'Press one to hear a song, two to receive an SMS.'

    twilio_response = Response()
    with twilio_response.gather(action='/respond_digits/', numDigits=1) as g:
        g.say(msg)
        g.pause(length=3)
        g.say(msg)

    return twilio_response

# take appropriate action depending on what number user dialed
@twilio_view
def handle_response_digits(request):
 
    twilio_request = decompose(request)
    digits = twilio_request.digits

    twilio_response = Response()
 
    if digits == '2':
        # twilio_response.play('http://bit.ly/phaltsw')
        number = request.POST.get('From', '')
        twilio_response.say('A text message is on its way. Daaaaaaaaaaaaaaamn Daniel! Peace out yo')
        twilio_response.sms('Daaaaaaaaaaaaaaamn Daniel!', to=number)
 
    elif digits == '1':
        # twilio_response.play('http://bit.ly/phaltsw')
        # twilio_response.play('https://p.scdn.co/mp3-preview/934da7155ec15deb326635d69d050543ecbee2b4')
        # twilio_response.play('https://p.scdn.co/mp3-preview/934da7155ec15deb326635d69d050543ecbee2b4')
        twilio_response.play('https://demo.twilio.com/hellomonkey/monkey.mp3')
        
        # number = request.POST.get('From', '')
        # twilio_response.say('I got you bruh, sending you a text in a bit. PEACE!')
        # twilio_response.sms('You looking lovely today!', to=number)

    # If the caller pressed invalid input
    else:
        # twilio_response.say('Incorrect Number Pressed')
        return redirect("/gather")
 
    return twilio_response

