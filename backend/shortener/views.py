from shortener.models import Shortener
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shortener.serializers import ShortenerSerializer


class CreateShortUrlView(APIView):
    def get(self, request, *args, **kwargs):
        shorteners = Shortener.objects.filter()
        serializer = ShortenerSerializer(shorteners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            # 'short_url': request.data.get('short_url'),
            'full_url': request.data.get('full_url'),
            # 'created_at': request.data.get('created_at'),
            # 'updated_at': request.data.get('updated_at')
        }
        serializer = ShortenerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
