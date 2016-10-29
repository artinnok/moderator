from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect, render
from django.conf import settings

from core.models import User


class AuthorizeView(APIView):
    url = ('https://oauth.vk.com/authorize?'
           'client_id={client_id}&'
           'display=page&'
           'redirect_uri={redirect_uri}&'
           'scope={scope}&'
           'response_type=token&'
           'v=5.59')

    def get(self, request, *args, **kwargs):
        return redirect(self.url.format(
            client_id=settings.CLIENT_ID,
            redirect_uri=settings.REDIRECT_URI,
            scope='wall,offline'
        ))


class CallbackView(APIView):
    def get(self, request, *args, **kwargs):
        access_token = request.query_params['access_token']
        user_id = request.query_params['user_id']
        User.objects.update_or_create(
            user_id=user_id,
            defaults={'access_token': access_token}
        )
        return Response('Вы авторизованы!')


class RedirectView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'api/redirect.html')
