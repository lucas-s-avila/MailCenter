from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden

from dashboard.models import Email

def update_status(request, email_id):
    email = get_object_or_404(Email, pk=email_id)
    if request.method == 'PATCH':
        status = request.POST['status']
        if status is not None:
            email.status = status
            email.save()
            return HttpResponse('Ok')
        return HttpResponseBadRequest('Status not found')
    return HttpResponseForbidden('Method not allowed')
    
    
