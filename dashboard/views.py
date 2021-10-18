import json

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

from dashboard.models import Email

@csrf_exempt
def update_status(request, email_id):
    email = get_object_or_404(Email, pk=email_id)
    if request.method == 'PATCH':
        status = json.loads(request.body.decode('utf-8')).get('status')
        if status is not None:
            email.status = status
            email.save()
            return HttpResponse('Ok')
        return HttpResponseBadRequest('Status not found')
    return HttpResponseForbidden('Method not allowed')
    
    
