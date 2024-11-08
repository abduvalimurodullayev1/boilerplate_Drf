from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.models import VersionHistory
from apps.common.api_endpoints.VersionHistory.serializers import VersionHistorySerializer


class VersionHistoryView(APIView):
    serializer_class = VersionHistorySerializer

    def get(self, request):
        query = VersionHistory.objects.first()
        data = self.serializer_class(query).data
        return Response(data=data, status=status.HTTP_200_OK)


__all__ = [
    'VersionHistoryView'
]
