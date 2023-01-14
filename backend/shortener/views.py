from shortener.models import Shortener
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shortener.serializers import ShortenerSerializer
from django.shortcuts import redirect


class CreateShortUrlView(APIView):

    def post(self, request, *args, **kwargs):
        data = {
            'full_url': request.data.get('full_url'),
        }
        serializer = ShortenerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            result = self.request.build_absolute_uri('/') + serializer.instance.short_url
            return Response({'result': result}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectUrlView(APIView):
    def get(self, request, *args, **kwargs):
        shortener = Shortener.objects.get(short_url=kwargs['shortened_part'])
        return redirect(shortener.full_url)
