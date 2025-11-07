

from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import redis

@api_view(["GET"])
def health_check(request):
    # Check DB
    try:
        connection.cursor()
    except Exception:
        return Response({"status": "error", "service": "db"}, status=500)

    # Check Redis
    try:
        redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
        ).ping()
    except Exception:
        return Response({"status": "error", "service": "redis"}, status=500)

    return Response({"status": "ok"}, status=200)
