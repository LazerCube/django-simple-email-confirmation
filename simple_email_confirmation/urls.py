from django.conf.urls import url
from simple_email_confirmation import views

app_name = 'simple_email_confirmation'
urlpatterns = [
    url(r'^confirm-email/(?P<confirmation_key>[\w-]+)/$', views.confirm_email, name='confirm_email')
]
