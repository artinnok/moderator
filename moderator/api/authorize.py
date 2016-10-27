from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.conf import settings
import requests

from core.models import Token


class AuthorizeView(APIView):
    url = 'https://oauth.vk.com/authorize?client_id={client_id}&display=page&redirect_uri={redirect_uri}&scope={scope}&response_type=token&v=5.59'

    def get(self, request, *args, **kwargs):
        return redirect(self.url.format(
            client_id=settings.CLIENT_ID,
            redirect_uri=settings.REDIRECT_URI,
            scope='wall,offline,messages,groups'
        ))


class CallbackView(APIView):
    url = 'https://oauth.vk.com/access_token?client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&code={code}'

    def get(self, request, *args, **kwargs):
        code = request.query_params['code']
        r = requests.get(self.url.format(
            client_id=settings.CLIENT_ID,
            client_secret=settings.CLIENT_SECRET,
            redirect_uri=settings.REDIRECT_URI,
            code=code
        ))
        json = r.json()
        Token.objects.update_or_create(
            access_token=json['access_token'],
            defaults=json
        )
        return Response('ok')
