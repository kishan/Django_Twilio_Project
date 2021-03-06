from django.conf.urls import url

from . import views


app_name = 'twilio_app'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^sms', views.sms, name='sms'),
    url(r'^ring', views.ring, name='ring'),

    url(r'^gather', views.gather_digits, name='gather'),
    url(r'^respond_digits', views.handle_response_digits, name='respond_digits'),
    url(r'^handle_recording', views.handle_recording, name='handle_recording'),

]


    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
