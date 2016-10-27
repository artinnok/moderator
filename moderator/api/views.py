from rest_framework.views import APIView
from rest_framework.response import Response
import requests


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
        parameters = 'owner_id={}&comment_id={}'.format(17127532, 1951)
        token = '06112913f955ade0d3e65acaaa58bf41d429b479920eb167f58d1f3bce7ed2d72c7c75b237c2ece9b291d'
        r = self.fetch(method, parameters, token)
        return Response(r)


class PermissionsView(DeleteView):
    def get(self, request, *args, **kwargs):
        method = 'account.getAppPermissions'
        parameters = ''
        token = '06112913f955ade0d3e65acaaa58bf41d429b479920eb167f58d1f3bce7ed2d72c7c75b237c2ece9b291d'
        r = self.fetch(method, parameters, token)
        return Response(r)
