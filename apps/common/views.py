import redis

from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Configure Redis connection
redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
)


@api_view(["GET"])
def health_check_redis(request):
    try:
        # Check Redis connection
        redis_client.ping()
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    except redis.ConnectionError:
        return Response(
            {"status": "error", "message": "Redis server is not working."},
            status=status.HTTP_400_BAD_REQUEST,
        )
