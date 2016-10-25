from rest_framework.views import APIView
from django.shortcuts import redirect
from django.conf import settings


class AuthorizeView(APIView):
    url = 'https://oauth.vk.com/authorize?client_id={client_id}&display=page&redirect_uri={redirect_uri}&scope=friends&response_type=code&v=5.59'

    def get(self, request, *args, **kwargs):
        return redirect(self.url.format(
            client_id=settings.CLIENT_ID,
            redirect_uri=settings.REDIRECT_URI
        ))


class CallbackView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.query_params)
