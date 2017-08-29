from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from simple_email_confirmation.models import EmailAddress

@login_required
def confirm_email(request, confirmation_key):
    try:
        email = request.user.confirm_email(confirmation_key)
    except EmailAddress.DoesNotExist:
         raise Http404("Confirmation reference not found! Either this link has expired or is invalid. Please request a new confirmation url.")
    return render(request, 'simple_email_confirmation/views/confirm_email.html', {'email': email})
