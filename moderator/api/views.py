from rest_framework.views import APIView
from rest_framework.response import Response


class AuthorizeView(APIView):
    def get(self, request, *args, **kwargs):
        print("hello")
        return Response("ok")