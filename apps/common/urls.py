from django.urls import path

from apps.common.views import health_check

app_name = "common"

urlpatterns = [

    path("health-check/redis/", health_check, name="health-check-redis"),
]
