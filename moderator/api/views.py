from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from core.models import Token


class DeleteView(APIView):
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'

    def fetch(self, method, parameters, token):
        return requests.get(self.url.format(
            method_name=method,
            parameters=parameters,
            access_token=token
        )).json()

    def get(self, request, *args, **kwargs):
        method = 'wall.deleteComment'
        parameters = 'owner_id={}&comment_id={}'.format(-112088372, 41)
        token = Token.objects.last().access_token
        r = self.fetch(method, parameters, token)
        return Response(r)


class PermissionsView(DeleteView):
    def get(self, request, *args, **kwargs):
        method = 'account.getAppPermissions'
        parameters = ''
        token = Token.objects.last().access_token
        r = self.fetch(method, parameters, token)
        return Response(r)
