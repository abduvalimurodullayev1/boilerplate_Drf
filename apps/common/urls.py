from django.urls import path

from apps.common.api_endpoints import *
from apps.common.views import health_check_redis

app_name = "common"

urlpatterns = [

    path("health-check/redis/", health_check_redis, name="health-check-redis"),
]
